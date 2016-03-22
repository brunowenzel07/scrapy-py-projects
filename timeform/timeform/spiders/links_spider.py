#! usr/bin/python

import re

from scrapy.http.request import Request
from scrapy.spiders import Spider
from scrapy.selector import Selector
# import logging

from timeform.items import linkItem
from datetime import date, timedelta

linkxpath = '/html/body/div/div[2]/div/div[3]/div/div/div[1]/div[2]/div/div/ul/li/a/@href'
titlexpath = '/html/body/div/div[2]/div/div[3]/div/div/div[1]/div[2]/div/div/ul/li'

def replace_racedate(sometext):
	newtext = '20' + sometext[1:3] + "-" + sometext[3:5] + "-" + sometext[5:]
	return newtext

def calc_distance(miles, furlongs, yards):
        if miles == "":
            m = 0
        else:
            m = float(miles)
        if furlongs == "":
            f = 0
        else:
            f = float(furlongs)
        if yards == "":
            y = 0
            distance = round((m * 8) + f, 2)
        else:
            y = float(yards)
            new_y = round((y/220), 2)
            distance = round((m * 8) + f + new_y, 2)
        return distance

def create_starturls():
	newpages = []
	n = 0
	# IMPORTANT - ADJUST this figure for number of days you want scraped
	while n < 365:
		# IMPORTANT - ADJUST the date in date() for the start date to be scraped
		strdate = (date(2014,01,01)+timedelta(n)).strftime('%Y%m%d')
		newpage = 'http://form.horseracing.betfair.com/daypage?date=%s' % strdate
		newpages.append(newpage)
		n += 1
	return newpages

class timeformSpider(Spider):
	name = "links"
	download_delay = 0.2
	allowed_domains = ["form.horseracing.betfair.com"]
	start_urls = create_starturls()

	# def __init__(self, name=None, **kwargs):
	# 	ScrapyFileLogObserver(open("spider_error.log", 'w'), level=logging.ERROR).start()

	# 	super(testformSpider, self).__init__(name, **kwargs)

	def parse(self, response):
		# each response.url is a daypage link
		item = linkItem()

		# each racelist is a list of racepage urls
		titlelist = response.xpath(titlexpath + '/@title').extract()
		reflist = response.xpath(titlexpath + '/a/@href').extract()

		for title, ref in zip(titlelist, reflist):
			# print title
			match = re.search(r'(^[a-z0-9]*)\s([0-9yds]*)(.*)\s\|\s(.*)\srunners', title)
			if match:
				ms_fs = match.group(1)
				ms_match = re.search(r'([0-9])m', ms_fs)
				fs_match = re.search(r'([0-9])f', ms_fs)
				if ms_match:
					miles = ms_match.group().replace("m","")
				else:
					miles = ""
				if fs_match:
					furlongs = fs_match.group().replace("f","")
				else:
					furlongs = ""
				yards = match.group(2).replace("yds","")
				item['disttext'] = (match.group(1) + " " + match.group(2)).strip()
			 	item['distance'] = calc_distance(miles, furlongs, yards)
				item['racetype'] = match.group(3).strip()
				item['runners'] = int(match.group(4).strip())
			codes = re.findall('1.[0-9]+.[0-9]+.[0-9]+', ref)
			codes = "".join(codes)
			item['raceID'] = re.sub("\.","",codes)
			codes = codes.split(".")
			item['racelink'] = ref.replace("/raceresult?raceId=", "")
			item['racecourse'] = int(codes[1])
			item['racedate'] = replace_racedate(codes[2])
			item['raceno'] = int(codes[3])
			yield item
		return
