#!/usr/bin/env python

import scrapy
import csv
import json
import re
import string
from abebooks.items import Abebooks2Item

class AbebooksSpider(scrapy.Spider):
    name = "abebooks_3"
    allowed_domains = ["abebooks.co.uk"]
    # Scrapes all priced signed first edition books for 100 great victorians
    # each entered not as authors but as keywords.
    # With next page toggled out in parse will gather highest 50 priced books only.
    with open("/home/benjamin/Documents/retail/data/victorians/victorians_5.json", 'r') as jsonfile:
        victorians = json.load(jsonfile)
        url_list = []
        for eachkey in victorians.keys():
            # print eachkey
            url = victorians[eachkey]['high_price_url']
            url_list.append(url)
        start_urls = url_list

    def parse(self, response):
		for eachbook in response.xpath('//div[contains(@id, "book-")]'):
		    item = Abebooks2Item()
		    match = re.search('kn=(.*)&recentlyadded', response.url).group(1)
		    print match
		    item['victorian'] = match.replace("+", "_").replace("%22", "")
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
		# next_page = response.xpath('//a[contains(@id, "bottombar-page-next")]/@href')
		# if next_page:
		#     url = response.urljoin(next_page[0].extract())
		#     yield scrapy.Request(url, self.parse)
