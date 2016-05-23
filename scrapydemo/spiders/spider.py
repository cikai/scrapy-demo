# -*- coding: utf-8 -*-
import scrapy


class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["sina.com"]
    start_urls = (
        'http://www.sina.com/',
    )

    def parse(self, response):
        pass
