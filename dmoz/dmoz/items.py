# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.loader.processor import TakeFirst, MapCompose, Compose, Join
from w3lib.html import remove_tags


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()

class daydownItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()

