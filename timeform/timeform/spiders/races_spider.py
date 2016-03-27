#! usr/bin/python

import re
import string
import unicodecsv

from scrapy.http.request import Request
from scrapy.spiders import Spider
from scrapy.selector import Selector
import logging

from timeform.items import raceItem
from datetime import date, timedelta

orig_path = '/home/benjamin/Documents/programming/scrapy/timeform/data/csv/links2014.csv'
racexpath = '/html/body/div/div[2]/div/div[2]/div/div/div[2]'
racextraxpath = '/html/body/div/div[2]/div/div[3]/div/div/div[2]'

def amend_wintime(wintime):
	data = re.findall(r'([\d+]+).', wintime)
	if len(data) < 2:
		return
	elif len(data) == 2:
		wintime = data[0] + '.' + data[1]
	elif len(data) == 3:
		wintime = str((int(data[0]))*60 + (int(data[1]))) + '.' + data[2]
	elif len(data) > 3:
		return
	else:
		return
	return wintime

def read_starturls():
	newpages = []
	base_url = "http://form.horseracing.betfair.com"
	with open(orig_path, 'r') as infile:
		csvreader = unicodecsv.reader(infile, delimiter=",")
		csvlist = list(csvreader)
		for eachrow in csvlist[1:]:
			newpages.append(base_url + "/raceresult?raceId=" + eachrow[6])
	return newpages

def amend_going(going):
	goingreps = {' to ': '-', 'all-weather' : "", 'chase course' : "", 'hurdles course' : "",
				 'first race' : "", 'remainder' : '', '(new course)' : "", 'first 2 races' : "",
				 'first 3 races' : "", 'first 4 races' : "", 'first 5 races' : "",
				 'straight course' : '', 'round course' : ''}
	going = translate(going, goingreps)
	return going

def get_raceclass(title):
	match = re.search(r"\((\w)\)", title)
	if match:
		raceclass = re.sub("[\(\)]","", match.group())
	else:
		raceclass = ""
	return raceclass

def get_gender(title):
	title = title.lower()
	match = re.search(r"colts \& fillies", title)
	match2 = re.search(r"fillies and mares", title)
	match3 = re.search(r"colts", title)
	match4 = re.search(r"fillies", title)
	match5 = re.search(r"mares", title)
	if match:
		gender = "colts and fillies"
	elif match2:
		gender = "fillies and mares"
	elif match3:
		gender = "colts"
	elif match4:
		gender = "fillies"
	elif match5:
		gender = "mares"
	else:
		gender = ""
	return gender

def translate(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

class timeformSpider(Spider):
	name = "races"
	allowed_domains = ["form.horseracing.betfair.com"]
	newpages = []
	base_url = "http://form.horseracing.betfair.com"

	with open(orig_path, 'r') as infile:
		csvreader = unicodecsv.reader(infile, delimiter=",")
		csvlist = list(csvreader)
		for eachrow in csvlist[1:]:
			newpages.append(base_url + "/raceresult?raceId=" + eachrow[6])
	start_urls = newpages

	# def __init__(self, name=None, **kwargs):
	# 	ScrapyFileLogObserver(open("spider_error.log", 'w'), level=logging.ERROR).start()

	# 	super(testformSpider, self).__init__(name, **kwargs)

	def parse(self, response):
		# each response url is a racepage url
		item = raceItem()

		codes = re.findall('1.[0-9]+.[0-9]+.[0-9]+', response.url)
		for each in codes:
			item['raceID'] = re.sub("\.","", each)

		racetitle = response.xpath(racexpath + '/p[@class="race-description"]/text()').extract()
		for each in racetitle:
			title = each.strip()
			item['racetitle'] = title
			item['raceclass'] = get_raceclass(title)
			item['gender'] = get_gender(title)

		racedets = response.xpath(racexpath + '/p/span/text()').extract()
		for each in racedets:
			if each[0:2] == 'Go':
				going = re.sub("[\|,\;\,\:]","", each[7:]).rstrip().lower()
				going_list = amend_going(going).strip().split(" ")
				item['going'] = going_list[0]
			elif each[0:2] == 'Ag':
				item['age'] = each[5:].replace("|","").rstrip()
			elif each[0:2] == 'To':
				item['prize'] = each[20:].replace("|","").rstrip()
			elif each[0:2] == 'Ra':
				item['racetype2'] = each[11:].replace("|","").rstrip()
			else:
				pass

		ranandtime = response.xpath(racextraxpath + '/p[1]/text()').extract()
		for each in ranandtime:
			neweach = re.findall('([0-9]+).*\:\s(.*)', each)
			for each in neweach:
				item['ran'] = each[0]
				wintime = each[1]
				item['wintime'] = amend_wintime(wintime)

		if len(response.xpath(racextraxpath + '/p/text()')) == 3:
			bf_ovrnd = response.xpath(racextraxpath + '/p[2]/text()').extract()
			for each in bf_ovrnd:
				item['bf_ovrnd'] = each.replace('Betfair SP Overround/Underround: ','').replace('%','')

			ind_ovrnd = response.xpath(racextraxpath + '/p[3]/text()').extract()
			for each in ind_ovrnd:
				item['ind_ovrnd'] = each.replace('Industry overround: ','').replace('%','')

		elif len(response.xpath(racextraxpath + '/p/text()')) == 2:
			ind_ovrnd = response.xpath(racextraxpath + '/p[2]/text()').extract()
			for each in ind_ovrnd:
				item['bf_ovrnd'] = ""
				item['ind_ovrnd'] = each.replace('Industry overround: ','').replace('%','')

		else:
			pass

		yield item
		return
