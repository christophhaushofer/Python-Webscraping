# allstays.py
# Lowes
# Created by Noah Christiano on 7/21/2014.
# noahchristiano@rochester.edu

# -*- coding: utf-8 -*-
#gets lowe's locations from http://www.allstays.com/c/lowes-locations.htm
#website does not indicate how accurate this data is
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from locations.items import LocationsItem


class AllstaysSpider(CrawlSpider):
	print 'Crawling allstays.com'
	name = 'allstays'
	allowed_domains = ['www.allstays.com']
	start_urls = ['http://www.allstays.com/c/lowes-locations.htm']
	
	rules = (
		Rule(LinkExtractor(allow_domains='www.allstays.com', restrict_xpaths='//div[@id="content"]//a', unique=True, deny_extensions='/c/road-guides.htm'), callback='parse_item', follow=False),
	)

	def parse_item(self, response):
		if response.url.endswith('-map.htm') or response.url.endswith('DL/') or response.url.endswith('road-guides.htm'):
			return
		state = response.xpath('//div[@id="content"]/h1/text()').extract()[0][19:]
		towns = response.xpath('//div[@id="content"]/h3/text()').extract()
		addresses = response.xpath('//div[@id="content"]/p/text()').extract()
			 
		stores = []
		for x in range(0, len(towns)):
			store = LocationsItem()
			store['state'] = state
			store['town'] = towns[x]
			store['address'] = addresses[2*x]
			store['store_number'] = addresses[2*x + 1][16:20]
			stores.append(store)
		return stores

#unique(fn:not(fn:ends-with(url, '-maps.htm'),
