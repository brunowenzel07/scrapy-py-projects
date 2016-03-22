# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst
from scrapy.utils.markup import remove_entities

class linkItem(Item):
	raceID = Field() # racelink without dots
	racelink = Field()
	racecourse = Field()
	racedate = Field()
	raceno = Field()
	disttext = Field()
	distance = Field()
	racetype = Field()
	runners = Field()
	pass

class raceItem(Item):
	raceID = Field() # racelink without dots
	racetitle = Field()
	raceclass = Field()
	gender = Field()
	going = Field()
	age = Field()
	prize = Field()
	racetype2 = Field()
	ran = Field()
	wintime = Field()
	bf_ovrnd = Field()
	ind_ovrnd = Field()	
	pass

class link2Item(Item):
	raceID = Field() # racelink without dots
	racelink = Field()
	racecourse = Field()
	racedate = Field()
	raceno = Field()
	disttext = Field()
	distance = Field()
	racetype = Field()
	runners = Field()
	racetitle = Field()
	raceclass = Field()
	gender = Field()
	going = Field()
	age = Field()
	prize = Field()
	racetype2 = Field()
	ran = Field()
	wintime = Field()
	bf_ovrnd = Field()
	ind_ovrnd = Field()
	pass

class resultItem(Item):
	raceID = Field() # racelink without dots
	position = Field()
	draw = Field()
	distbtn = Field()
	totdistbtn = Field()
	rhID = Field()
	racehorse = Field()
	age = Field()
	weight = Field()
	offrtg = Field()
	eqpmnt = Field()
	jockey = Field()
	allwnce = Field()
	trainer = Field()
	hi_ir = Field()
	lo_ir = Field()
	bsp = Field()
	isp = Field()
	place = Field()
	pass

