# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from myspider import settings
import requests

class MyspiderPipeline(object):
    def process_item(self, item, spider):
        dir_name = settings.IMAGES_STORE
        if 'img_url' in item:
            img_path = '%s/%s.jpg' %(dir_name , item['img_name'])
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            if os.path.exists(img_path):
                return item
            with open(img_path, 'wb') as handle:
                response = requests.get(url = item['img_url'])
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
        return item
