# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.item import Item, Field

class Product(Item):
    name = Field()


class StephanisSpider(CrawlSpider):
    name = "stephanis"
    allowed_domains = ["stephanis.com.cy"]
    start_urls = ['http://www.stephanis.com.cy/']

    rules = (Rule(SgmlLinkExtractor(), callback='parse_url', follow=False), )

    def parse_url(self, response):
        #for url in response.xpath('//a/@href').extract():
            #yield scrapy.Request(url, callback=self.parse)
            #print url
        pass