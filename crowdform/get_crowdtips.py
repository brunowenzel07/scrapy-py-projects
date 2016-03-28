# get_crowdtips.py
import re
import csv
from crowdform.items import CrowdformItem

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))

mydate = raw_input("Please enter str_date: ")
document = "crowdtips_" + mydate + ".txt"
csv_doc = "crowdtips_" + mydate + ".csv"

with open(document) as input_file:
	# initialise empty lists
	items = []
	newdata = []
	# opens file and reads lines into a list (note that file.read() would put the content into a string)
	data = input_file.readlines()
	# for each line
	for eachline in data:
		# remove all unwanted whitespace
		eachline = ' '.join(eachline.split())
		# only accept true lines, not blank lines, into empty list  
		if eachline:	
			newdata.append(eachline)
		else: pass
	# remove silly bookmaker advert for william hill
	del newdata[11:14]
	# split newdata into each group of 11 items
	for eachrace in chunker(newdata, 11):
		item = CrowdformItem()	
		item['bestbookie'] = eachrace[5]
		item['bestprice'] = eachrace[6]
		item['num_all_tips'] = eachrace[8]
		item['num_comments'] = eachrace[9]
		item['num_sel_tips'] = eachrace[8]
		item['racecourse'] = eachrace[0]
		item['racedate'] = eachrace[1]
		item['racehorse'] = eachrace[2]
		item['racetime'] = eachrace[1]			
		item['percentage'] = eachrace[8]		
		items.append(item)
	fieldnames = ['bestbookie', 'bestprice', 'racetime', 'num_comments', 'racehorse', 'num_sel_tips', 'bestbookie',
				  'percentage', 'racedate', 'bestprice']
	print fieldnames
	# print items[0]
	with open(csv_doc, "w") as output_file: 
		dict_writer = csv.DictWriter(output_file, fieldnames)
		# dict_writer.writeheader(fieldnames)
		dict_writer.writerows(output_file)
