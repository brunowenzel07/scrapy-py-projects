#!/usr/bin/env python

import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz_3"
    allowed_domains = ["dmoz.org"]
    start_urls = ["http://www.dmoz.org/Computers/Programming/Languages/Python/",]

    def parse(self, response):
        for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_articles_follow_next_page)

	def parse_articles_follow_next_page(self, response):
	    for article in response.xpath("//article"):
	        item = ArticleItem()

	        ... extract article data here

	        yield item

	    next_page = response.css("ul.navigation > li.next-page > a::attr('href')")
	    if next_page:
	        url = response.urljoin(next_page[0].extract())
	        yield scrapy.Request(url, self.parse_articles_follow_next_page)

