# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FindtripItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    site = scrapy.Field()
    company = scrapy.Field()
    airports = scrapy.Field()
    passtime = scrapy.Field()
    price = scrapy.Field()
    flight_leave_time = scrapy.Field()
    flight_arrive_time = scrapy.Field()
    flight_time = scrapy.Field()
    discount = scrapy.Field()
    plane = scrapy.Field()
