# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from wikiscrape.items import WikiscrapeItem

class Wikispider(scrapy.Spider):
    name = "wikispider1"
    allowed_domains = ["https://en.wikipedia.org/wiki"]
    start_urls = ["https://en.wikipedia.org/wiki/Category:Women_of_the_Victorian_era"]

    def parse(self, response):
        items = []
        sel = Selector(response)
        sites = sel.xpath('//div[@class="mw-category-group"]//li')
        
        for site in sites:
            item = WikiscrapeItem()
            item['title'] = site.xpath('a/text()').extract()
            items.append(item)

        return items

        # for sel in response.xpath('//div[@class="mw-category-group"]//li/a[@title]'):
        #     item = WikiscrapeItem
        #     item['title'] = sel.xpath('/a/@title').extract()
        #     item['href'] = sel.xpath('/a/@href').extract()
        #     # print title, href
        #     yield item
