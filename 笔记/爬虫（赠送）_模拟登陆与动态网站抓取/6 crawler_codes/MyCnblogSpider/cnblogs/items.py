# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnblogsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    linkmd5id = scrapy.Field()    #链接的md5值，作为数据库的index
    title = scrapy.Field()        #博客标题
    link = scrapy.Field()         #博客链接
    desc = scrapy.Field()         #博客描述
    read_num = scrapy.Field()     #阅读数
    comment_num = scrapy.Field()  #评论数
    pass
