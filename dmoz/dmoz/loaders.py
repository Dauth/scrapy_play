from scrapy.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst, MapCompose, Compose, Join
from w3lib.html import remove_tags, replace_escape_chars

def filter_link(input_link):
    links_list = ['uploaded', 'baidu']
    for link in links_list:
        if link in input_link:
            return input_link
    return None

class DmozLoader(ItemLoader):
    default_out_processor = TakeFirst()
    content_in = MapCompose(remove_tags, replace_escape_chars, unicode.strip)
    # content_out = Join()
    title_in = MapCompose(unicode.strip)
    link_in = MapCompose(unicode.strip)

class daydownLoader(ItemLoader):
    title_in = MapCompose(remove_tags, replace_escape_chars, unicode.strip)
    link_in = MapCompose(filter_link, remove_tags, replace_escape_chars, unicode.strip)

