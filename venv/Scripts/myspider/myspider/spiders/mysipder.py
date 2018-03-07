import scrapy
import re
from scrapy import Selector
from myspider.items import MyspiderItem

class MySpider(scrapy.Spider):
    name = "myspider"

    def __init__(self):
        #图片链接信息
        self.server_link = 'http://www.hldm123.cc/'
        self.allowed_domains = ['www.hldm123.cc/']
        self.start_urls = ['http://www.hldm123.cc/']
        #正则表达式
        self.pattern_img = re.compile('')

    def start_requests(self):
        yield scrapy.Request(url = self.start_urls[0], callback = self.parse)

    def parse(self, response):

        html = Selector(response)
        images_urls = html.xpath('//li/a[1]/img/@original').extract()
        images_name = html.xpath('//li/a[1]/p/text()').extract()

        for index in range(len(images_urls)):
            item = MyspiderItem()
            item['img_url'] = images_urls[index]
            item['img_name'] = images_name[index]
#            print('name:%s--------url:%s' %(item['img_name'], item['img_url']))
            yield item

#        for index in range(len(urls)):
#            item = MyspiderItem()
#            item['link_url'] = urls[index]

 #       for uu in urls:
 #           print('urls:-----------------------%s' %uu)

#    def parse(self, response):
#        # link_urls = response.xpath('//dd/a[1]/@href').extract()
#        dir_names = response.xpath('//dd/a[1]/text()').extract()
#        for each_name in dir_names:
#            print(each_name)

