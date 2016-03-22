# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy



# class WikiscrapeItem(scrapy.Item):
#     # define the fields for your item here like:
#     category = scrapy.Field()
#     content = scrapy.Field()
#     image = scrapy.Field()
#     link = scrapy.Field()
#     reference = scrapy.Field()
#     page_id = scrapy.Field()
#     parent_id = scrapy.Field()
#     revision_id = scrapy.Field()
#     summary = scrapy.Field()
#     title = scrapy.Field()
#     url = scrapy.Field()
#     pass

class WikiscrapeItem(scrapy.Item):
    title = scrapy.Field()
    # link = scrapy.Field()
    pass