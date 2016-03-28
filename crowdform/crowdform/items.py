# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrowdformItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bestbookie = scrapy.Field()
    bestprice = scrapy.Field()
    num_all_tips = scrapy.Field()
    num_comments = scrapy.Field()
    num_sel_tips = scrapy.Field()
    percentage = scrapy.Field()
    racecourse = scrapy.Field()
    racedate = scrapy.Field() 
    racetime = scrapy.Field()
    racehorse = scrapy.Field()
    pass

    # Event 	Top Selection 	  	  	  	Odds 	  	 
    # Event DateSort 	ConfidenceSort 	Win TipsSort 	RatingSort 	CommentsSort 	 
    