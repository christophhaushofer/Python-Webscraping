# pipelines.py
# Rap Genius
# Created by Noah Christiano on 8/15/2014.
# noahchristiano@rochester.edu

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GeniusPipeline(object):
    def process_item(self, item, spider):
        return item
