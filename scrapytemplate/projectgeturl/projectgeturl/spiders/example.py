# -*- coding: utf-8 -*-
import scrapy
from projectgeturl.items import myItem 

class ExampleSpider(scrapy.Spider):
    name = "example"
    inputfile = open('seed.txt', 'r')
    start_urls = [line.strip() for line in inputfile.readlines()]
    inputfile.close()

    def parse(self, response):
        item = myItem()
        try:
            item['myurl'] = response.url
            item['myhtml'] = response.body
            item['mystatus'] = 'fetched'
        except:
            item['mystatus'] = 'failed'
        yield item
