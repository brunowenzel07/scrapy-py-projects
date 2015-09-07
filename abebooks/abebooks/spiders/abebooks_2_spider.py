#!/usr/bin/env python

import scrapy
import csv
import json
import re
from abebooks.items import AbebooksItem

class AbebooksSpider(scrapy.Spider):
    name = "abebooks_2"
    allowed_domains = ["abebooks.co.uk"]
    # scrapes signed, inscribed keyword combo for 100 great victorians
    with open("/home/benjamin/Documents/retail/data/victorians/victorians_3.json", 'r') as jsonfile:
        victorians = json.load(jsonfile)
        for eachkey in victorians.keys():
            # print eachkey
            url_list = victorians[eachkey]['url_list']
            start_urls = url_list

    def parse(self, response):
		for eachbook in response.xpath('//div[contains(@id, "book-")]'):
		    item = AbebooksItem()
		    item['date'] = "".join(eachbook.xpath('./meta[contains(@itemprop, "datePublished")]/@content').extract()).strip()
		    item['title'] = "".join(eachbook.xpath('./meta[contains(@itemprop, "name")]/@content').extract())[:50].strip()
		    item['author'] = "".join(eachbook.xpath('./meta[contains(@itemprop, "author")]/@content').extract())[:30].strip()
		    item['price'] = "".join(eachbook.xpath('./div/div/h2/meta[1]/@content').extract()).strip()
		    item['about'] = "".join(eachbook.xpath('./meta[contains(@itemprop, "about")]/@content').extract()).strip()
		    item['publisher'] = "".join(eachbook.xpath('./meta[contains(@itemprop, "publisher")]/@content').extract()).strip()
		    item['bookFormat'] = "".join(eachbook.xpath('./meta[contains(@itemprop, "bookFormat")]/@content').extract()).strip()
		    item['currency'] = "".join(eachbook.xpath('./div/div/h2/meta[2]/@content').extract()).strip()
		    item['condition'] = "".join(eachbook.xpath('./div/div/h2/meta[3]/@content').extract()).strip()
		    item['availability'] = "".join(eachbook.xpath('./div/div/h2/meta[4]/@content').extract()).strip()
		    yield item
		next_page = response.xpath('//a[contains(@id, "bottombar-page-next")]/@href')
		if next_page:
		    url = response.urljoin(next_page[0].extract())
		    yield scrapy.Request(url, self.parse)
