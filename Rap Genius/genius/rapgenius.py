# rapgenius.py
# Rap Genius
# Created by Noah Christiano on 8/15/2014.
# noahchristiano@rochester.edu

from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from genius.spiders.verifiedArtists import VerifiedartistsSpider
from scrapy.utils.project import get_project_settings

items = []

def add_item(item):
	items.append(item)

def convertData(set):
	group = []
	class verified():
		id = 0
		name = ''
		url = ''
	for i in set:
		new = verified()
		iq = i['iq']
		new.iq = int(iq.replace(',', ''))
		new.url = i['url']
		new.name = i['name']
		group.append(new)
	return group

spider = VerifiedartistsSpider(domain='rapgenius.com')
settings = get_project_settings()
crawler = Crawler(settings)
crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
crawler.signals.connect(add_item, signals.item_scraped)
crawler.configure()
crawler.crawl(spider)
crawler.start()
#log.start()
reactor.run()

set = convertData(items)
set.sort(key=lambda x: x.iq, reverse=True)

for i in range(0, 30):
	print str(i+1) + ': ' + str(set[i].iq) + ' ' + set[i].name# + ' ' + set[i].url
