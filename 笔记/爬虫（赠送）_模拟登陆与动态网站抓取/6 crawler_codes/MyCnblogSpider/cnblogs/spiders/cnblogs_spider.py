#coding=utf-8
import re
import json
from scrapy.selector import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from cnblogs.items import CnblogsItem

class CnblogsSpider(CrawlSpider):
    #定义爬虫的名称
    name = "CnblogsSpider"
    #定义允许抓取的域名,如果不是在此列表的域名则放弃抓取
    allowed_domains = ["cnblogs.com"]
    #定义抓取的入口url
    start_urls = [
    	"http://www.cnblogs.com/tornadomeet/default.html?page=1"
    ]

    # 定义爬取URL的规则，并指定回调函数为parse_item
    rules = [
        Rule(sle(allow=("/tornadomeet/default.html\?page=\d{1,}")), #此处要注意?号的转换，复制过来需要对?号进行转换。
			 follow=True, 
			 callback='parse_blog'),
    ]
    print "**********我是博客园爬虫，神奇的分割线**********"


    #定义回调函数
    #提取数据到Items里面，主要用到XPath和CSS选择器提取网页数据
    def parse_blog(self, response): 
        print "--------解析目录页面---------"
        for blog in response.xpath('//div[@class="day"]'):
            blog_item = CnblogsItem()
            blog_item['title'] = blog.xpath('.//div[@class="postTitle"]/a/text()').extract_first()
            blog_item['link'] = response.urljoin(blog.xpath('.//div[@class="postTitle"]/a/@href').extract_first())
            blog_item['desc'] = blog.xpath('.//div[@class="c_b_p_desc"]/text()').extract_first()
            blog_info = blog.xpath('.//div[@class="postDesc"]/text()').extract_first()
            blog_item['read_num'] = blog_info.split('(')[1].split(')')[0]
            blog_item['comment_num'] = blog_info.split('(')[2].split(')')[0]

            yield blog_item

            print blog_item['title']
            print blog_item['link']
            print blog_item['desc']
            print blog_item['read_num']
            print blog_item['comment_num']
