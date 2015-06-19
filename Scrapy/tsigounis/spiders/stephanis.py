# -*- coding: utf-8 -*-
import scrapy


class StephanisSpider(scrapy.Spider):
    name = "stephanis"
    allowed_domains = ["stephanis.com.cy"]
    start_urls = (
        'http://www.stephanis.com.cy/',
    )
    #Constructor
    def __init__(self):
        pass

    def parse(self, response):
        pass
