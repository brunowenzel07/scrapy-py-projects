#! usr/bin/python

import re
from string import replace
import unicodecsv

from scrapy.http.request import Request
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import XPathItemLoader, ItemLoader
from scrapy.loader.processors import Join, MapCompose, Identity
import logging

from timeform.items import resultItem
from datetime import date, timedelta

orig_path = '/home/benjamin/Documents/programming/scrapy/timeform/data/csv/links2014.csv'
resultxpath = '/html/body/div/div[2]/div/div[3]/div/div/div/table/tbody/tr'

def translate(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

def remove_entities(sometext):
	newtext = re.sub('[\(\)\,\-\/]','',sometext)
	return newtext

def conv_to_int(sometext):
	if sometext == "":
		pass
	else:
		sometext = int(sometext)
	return sometext

def conv_to_float(sometext):
	if sometext == "":
		pass
	else:
		sometext = float(sometext)
	return sometext

def remove_from_rhID(sometext):
	newtext = sometext.replace("/horse?horseId=1.",'')
	return newtext

def remove_from_trainer(sometext):
	newtext = re.sub('[\,]','  ',sometext)
	return newtext

def amend_weight(sometext):
	weight = "".join(sometext).split("-")
	stones = int(weight[0]) * 14
	if len(weight) > 1:
		pounds = int(weight[1])
		weight = stones + pounds
	else:
		pounds = 0
		weight = stones + pounds
	weight = str(weight)
	return weight

def amend_distbtn(distbtn):
	distreps = {'\xc2' : '', '\xbd' : '.5', '\xbc' : '.25', '\xbe' : '.75', 'dh' : '', 'dht' : '',  'ns' : '.05', 'nse' : '.05', 's.h' : '.1', 'sh' : '.1', 'hd' : '.2', 'snk' : '.25', 'nk' : '.3', 'ds' : '30', 'dist' : '30'}
	distbtn = distbtn.encode('utf-8', 'ignore')
	distbtn = translate(distbtn, distreps)
	return distbtn

def read_starturls():
	newpages = []
	base_url = "http://form.horseracing.betfair.com//raceresult?raceId="
	with open(orig_path, 'r') as infile:
		csvreader = unicodecsv.reader(infile, delimiter=",")
		csvlist = list(csvreader)
		for eachrow in csvlist[1:]:
			newpages.append(base_url + eachrow[6])
	return newpages

class timeformSpider(Spider):
	name = "results"
	allowed_domains = ["form.horseracing.betfair.com"]
	start_urls = read_starturls()

	# def __init__(self, name=None, **kwargs):
	# 	ScrapyFileLogObserver(open("spider_error.log", 'w'), level=logging.ERROR).start()

	# 	super(testformSpider, self).__init__(name, **kwargs)

	def parse(self, response):
		# each response url is a racepage url
		item = resultItem()

		totdistbtn = 0.00

		codes = re.findall('1.[0-9]+.[0-9]+.[0-9]+', response.url)
		for each in codes:
			item['raceID'] = re.sub("\.","", each)

		rowpath = response.selector.xpath(resultxpath)
		# print type(rowpath) # <class 'scrapy.selector.unified.SelectorList'>
		for eachrow in rowpath:
		 	position = "".join(eachrow.xpath('.//td[1]/span[@class="pos"]/text()').extract()).strip()
			item['position'] = position
			draw = "".join(eachrow.xpath('.//td[1]/span[@class="draw"]/text()').extract()).strip()
			item['draw'] = remove_entities(draw)
			distbtn = "".join(eachrow.xpath('.//td[2]/text()').extract()).strip()
		 	distbtn = amend_distbtn(distbtn)
			item['distbtn'] = distbtn
			if distbtn == "":
				if position.isdigit():
					if position == '1':
						totdistbtn = 0.00
					else:
						totdistbtn = totdistbtn
				else:
					totdistbtn = ""
			else:
				totdistbtn += round(float(distbtn), 2)
			item['totdistbtn'] = totdistbtn
			rhID = "".join(eachrow.xpath('.//td[3]/a/@href').extract()).strip()
			item['rhID'] = remove_from_rhID(rhID)
			item['racehorse'] = "".join(eachrow.xpath('.//td[3]/a/text()').extract()).strip()
			age = "".join(eachrow.xpath('.//td[4]/text()').extract()).strip()
			item['age'] = age
			weight = "".join(eachrow.xpath('.//td[5]/span[@class="wgt"]/text()').extract()).strip()
			item['weight'] = amend_weight(weight)
			offrtg = "".join(eachrow.xpath('.//td[5]/span[@class="or"]/text()').extract()).strip()
			item['offrtg'] = remove_entities(offrtg)
			eqpmnt = "".join(eachrow.xpath('.//td[6]/text()').extract()).strip()
			item['eqpmnt'] = remove_entities(eqpmnt).strip()
			item['jockey'] = "".join(eachrow.xpath('.//td[7]/a[1]/text()').extract()).strip()
			allwnce = "".join(eachrow.xpath('.//td[7]/sup/text()').extract()).strip()
			item['allwnce'] = remove_entities(allwnce).strip()
			trainer = "".join(eachrow.xpath('.//td[7]/a[2]/text()').extract()).strip()
			item['trainer'] = remove_from_trainer(trainer)
			hi_ir = "".join(eachrow.xpath('.//td[8]/span[@class="high"]/text()').extract()).strip()
			item['hi_ir'] = remove_entities(hi_ir).strip()
			lo_ir = "".join(eachrow.xpath('.//td[8]/span[@class="low"]/text()').extract()).strip()
			item['lo_ir'] = remove_entities(lo_ir).strip()
			bsp = "".join(eachrow.xpath('.//td[9]/span[@class="bsp"]/text()').extract()).strip()
			item['bsp'] = remove_entities(bsp).strip()
			isp = "".join(eachrow.xpath('.//td[9]/span[@class="isp"]/text()').extract()).strip()
			item['isp'] = remove_entities(isp).strip()
			place = "".join(eachrow.xpath('.//td[10]/text()').extract()).strip()
			item['place'] = remove_entities(place).strip()
			yield item
		return
