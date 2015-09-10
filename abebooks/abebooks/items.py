# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AbebooksItem(scrapy.Item):
	# define the fields for your item here like:
	# meta = scrapy.Field()
	date = scrapy.Field()
	title = scrapy.Field()
	author = scrapy.Field()
	price = scrapy.Field()
	about = scrapy.Field()
	publisher = scrapy.Field()
	bookFormat = scrapy.Field()
	currency = scrapy.Field()
	condition = scrapy.Field()
	availability = scrapy.Field()
	pass

class Abebooks2Item(scrapy.Item):
	# define the fields for your item here like:
	# meta = scrapy.Field()
	victorian = scrapy.Field()
	date = scrapy.Field()
	title = scrapy.Field()
	author = scrapy.Field()
	price = scrapy.Field()
	about = scrapy.Field()
	publisher = scrapy.Field()
	bookFormat = scrapy.Field()
	currency = scrapy.Field()
	condition = scrapy.Field()
	availability = scrapy.Field()
	pass

class Abebooks3Item(scrapy.Item):
	# define the fields for your item here like:
	# meta = scrapy.Field()
	kw_pair = scrapy.Field()
	date = scrapy.Field()
	title = scrapy.Field()
	author = scrapy.Field()
	price = scrapy.Field()
	about = scrapy.Field()
	publisher = scrapy.Field()
	bookFormat = scrapy.Field()
	currency = scrapy.Field()
	condition = scrapy.Field()
	availability = scrapy.Field()
	pass
