# -*- coding: utf-8 -*-
import scrapy
class myItem(scrapy.Item):
    myurl = scrapy.Field(default="")
    myhtml = scrapy.Field(default="")
    mystatus = scrapy.Field(default="unfetched")
