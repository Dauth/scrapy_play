
# -*- coding: utf-8 -*-
import scrapy
import os
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MyasiantvspSpider(CrawlSpider):
    name = 'myasiantvsp'
    allowed_domains = ['myasiantv.com', 'vidnow.to', 'openload.co']
    start_urls = []
    with open("todownloadlinks.txt", 'rt') as infile:
        start_urls= [url.strip() for url in infile.readlines()]
    print (start_urls)
    rules = (
        Rule(LinkExtractor(restrict_css='.play > strong a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        myname = (response.css('.sumer_l > ul > li::text').extract()[0])
        mylink = (response.css('.dowload > a::attr(href)').extract())
        return{
            'name': myname,
            'link': mylink,
        }
