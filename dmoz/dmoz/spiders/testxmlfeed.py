# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider


class TestxmlfeedSpider(XMLFeedSpider):
    name = 'testxmlfeed'
    allowed_domains = ['testxmlfeed.com']
    start_urls = ['http://www.testxmlfeed.com/feed.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'item' # change it accordingly

    def parse_node(self, response, selector):
        i = {}
        #i['url'] = selector.select('url').extract()
        #i['name'] = selector.select('name').extract()
        #i['description'] = selector.select('description').extract()
        return i
