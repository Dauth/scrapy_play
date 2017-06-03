# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst, MapCompose, Compose
from scrapy.selector.unified import Selector, SelectorList
from dmoz.items import DmozItem
from dmoz.loaders import DmozLoader
from w3lib.html import replace_escape_chars, remove_tags

class TechnologySpider(scrapy.Spider):
    #this is the spider name and must be unique
    name = "dmoz"
    allowed_domains = ["dmoz.org"]

    #where the spider wdmozLoaderl start to crawl
    start_urls = (
        'http://www.dmoz.org/Computers/Programming/Languages/Python/Books/',
    )

    #method of spider, called with the downloaded Response object of each start url
    #response is the only arg passed to this method
    #method parses response data and extract the scrapped data and return it as ITEM
    # def parse(self, response):
        # item = DmozItem()
        # titles = response.css('.site-title::text').extract()
        # links = response.css('.title-and-desc > a::attr(href)').extract()
        # contents = [line.strip() for line in response.css('.site-descr::text').extract() if len(line.strip()) > 0]

        # for i, title in enumerate(titles):
            # item['title'] = title
            # item['link'] = links[i]
            # item['content'] = contents[i]
            # yield item

    # This is another way of of doing by using ItemLoader
    #Items provide the container of scraped data,  Item Loaders provide the mechanism for populating that container.
    # This will make each title,content, link on the same dict
    def parse(self, response):
        site_items = response.css('.site-item')
        for site_item in site_items:
            dmozLoader = DmozLoader(item = DmozItem(), selector = site_item)
            dmozLoader.add_css('title', '.site-title::text')
            dmozLoader.add_css('link', '.title-and-desc >a::attr(href)')
            dmozLoader.add_css('content', '.site-descr')
            yield dmozLoader.load_item() # method is called which actually returns the item populated with the data previously extracted and collected with the add_css


    # Note see how this method is constructed
    # This will make all titles, content, links on separate lists
    # def parse(self, response):
        # il = DmozLoader(item = DmozItem(), response = response)
        # il.add_css('title', '.site-title::text')
        # il.add_css('link', '.title-and-desc >a::attr(href)')
        # il.add_css('content', '.site-descr')
        # yield il.load_item() # method is called which actually returns the item populated with the data previously extracted and collected with the add_css
