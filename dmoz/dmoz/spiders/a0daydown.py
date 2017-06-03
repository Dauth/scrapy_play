# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dmoz.items import daydownItem
from dmoz.loaders import daydownLoader


class A0daydownSpider(CrawlSpider):
    name = '0daydown'
    allowed_domains = ['0daydown.com']
    start_urls = ['http://www.0daydown.com/category/tutorials/other',
                  'http://www.0daydown.com/category/tutorials/other/page/56']

    rules = (
        Rule(LinkExtractor(restrict_css='.focus > a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_css='.next-page > a'), follow=True),
    )

    def parse_item(self, response):
        loader = daydownLoader(item = daydownItem(), response = response)
        loader.add_css('title', '.article-title > a::text')
        loader.add_css('link', 'a::attr(href)')
        yield loader.load_item()

