from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_redis.spiders import RedisCrawlSpider


class DaydownCrawler(RedisCrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'daydowncrawler_redis'
    redis_key = 'daydowncrawler:start_urls'

    rules = (
        Rule(LinkExtractor(restrict_css='.focus > a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_css='.next-page > a'), follow=True),
    )

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(DaydownCrawler, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        return{
            'title': response.css('.article-title > a::text'),
            'link': response.css('a::attr(href)'),
        }
