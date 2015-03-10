# items.py
# Rap Genius
# Created by Noah Christiano on 8/15/2014.
# noahchristiano@rochester.edu

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Field, Item

class Artist(Item):
# define the fields for your item here like:
# name = scrapy.Field()
	name = Field()
	iq = Field()
	url = Field()
