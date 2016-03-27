# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from wikiscrape.items import WikiscrapeItem

class Wikispider(scrapy.Spider):
    name = "wikispider1"
    allowed_domains = ["https://en.wikipedia.org/wiki"]
    start_urls = ["https://en.wikipedia.org/wiki/Princess_Beatrice_of_the_United_Kingdom"]

    def parse(self, response):
        items = []
        sel = Selector(response)
        infoboxRows = sel.xpath('//table[@class="infobox vcard"]//tr')
        for row in infoboxRows:
        	item = WikiscrapeItem()
        	item['ibTitle'] = row.xpath('//th//text()').extract()
        	item['ibKey']   = row.xpath('//td//text()').extract()
        	items.append(item)  

		return items        	
