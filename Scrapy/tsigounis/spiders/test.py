from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field


class MyItem(Item):
    url = Field()


class MySpider(CrawlSpider):
    name = 'public'
    allowed_domains = ['stephanis.com.cy']
    start_urls = ['http://www.stephanis.com.cy']

    rules = (Rule(SgmlLinkExtractor(restrict_xpaths=('')), callback='parse_url', follow=False), )

    def parse_url(self, response):
        item = MyItem()
        item['url'] = response.url
        return item
