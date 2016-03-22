# scraper.py

import csv
import json
import pickle
import string
import wikipedia

def encodeList(someList):
	""" Gets around a frustrating encoding issue with lists."""
	newlist = []
	for each in someList:
		encodeditem = each.encode('utf-8')
		newlist.append(encodeditem)
	return newlist

def decodeList(someList):
	""" Gets around a frustrating encoding issue with lists."""
	newlist = []
	for each in someList:
		decodeditem = each.decode('utf-8')
		newlist.append(decodeditem)
	return newlist	

def writeContentTextFile(wikiPage):
	""" This is nice. Writes out a pure text representation of the Wikipedia page."""
	with open(wikiPage.title + ".txt", "w") as f:
		f.write(wikiPage.title.upper() + "\n")
		f.write(wikiPage.url + "\n" + "\n")
		f.write(wikiPage.content.encode('utf-8'))
		return

def writeLinksTextFile(wikiPage):
	""" Clear to read. Keeps things on individual lines and encoded."""		
	with open(wikiPage.title + " Links.txt", "w") as f:
		f.write("TITLE: " + wikiPage.title.encode('utf-8') + "\n")
		f.write("PAGE ID: " + wikiPage.pageid.encode('utf-8') + "\n")
		f.write("URL: " + wikiPage.url.encode('utf-8') + "\n")
		f.write("SUMMARY: " + wikiPage.summary.encode('utf-8') + "\n")
		f.write("CATEGORIES: " + "\n")
		for each in wikiPage.categories:
			f.write(each.encode('utf-8') + "\n") 
		f.write("REFERENCES: " + "\n")
		for each in wikiPage.references:
			f.write(each.encode('utf-8') + "\n") 
		f.write("IMAGE LINKS: " + "\n")
		for each in wikiPage.images:
			f.write(each.encode('utf-8') + "\n")
		f.write("LINKS: " + "\n")
		for each in wikiPage.links:
			f.write(each.encode('utf-8') + "\n")
		return

def readLinksTextFile(wikiPage):
	""" Works OK but adds a new line to everything. """
	with open(wikiPage.title + " Links.txt", "r") as f:
		data = f.readlines()
		# newdata = []
		for each in data:
			each.replace(r'\n', "")
			# newdata.append(each)
		return data

def createDict(wikiPage):
	newDict = {}
	newDict["Title"] = wikiPage.title.encode('utf-8')
	newDict["Page ID"] = wikiPage.pageid.encode('utf-8')
	newDict["URL"] = wikiPage.url.encode('utf-8')
	newDict["Summary"] = wikiPage.summary.encode('utf-8')
	newDict["Categories"] = encodeList(wikiPage.categories)
	newDict["References"] = encodeList(wikiPage.references)
	newDict["Image Links"] = encodeList(wikiPage.images)
	newDict["Links"] = encodeList(wikiPage.links)
	newDict["Content"] = wikiPage.content.encode('utf-8')
	return newDict

# def writePickleFile(someDict):
# 	""" Doesn't really work. """
# 	with open(someDict["Title"] + " Links.txt", 'wb') as handle:
# 		pickle.dump(someDict, handle)
# 		return

# def readPickleFile(someDict):
# 	""" Doesn't really work. """
# 	with open(someDict["Title"] + " Links.txt", 'rb') as handle:
# 		data = pickle.loads(handle.read())
# 		return data

def writeJsonFile(someDict):
	""" The JSON dump and load programs seems to work pretty well. """
	with open(someDict["Title"] + " Links.json", "w") as f:
		json.dump(someDict, f)
		return

def readJsonFile(someDict):
	""" The JSON dump and load programs seems to work pretty well. """
	with open(someDict["Title"] + " Links.json", 'r') as f:
		data = json.load(f)
		return data

def writeCsvFile(someDict):
	""" The dictionary is not structured suitably for a spreadsheet. Try to open with gedit.
	    This basic Csv writer program works. """  
	with open(someDict["Title"] + " Links.csv", 'wb') as f:
		w = csv.DictWriter(f, someDict.keys())
		w.writeheader()
		w.writerow(someDict)
		return

def readCsvFile(someDict):
	""" Doesn't work. """
	with open(someDict["Title"] + " Links.csv", 'r') as f:
		r = csv.DictReader(f, someDict.keys())
		r.readheader()
		r.readrow(someDict)
		return r

wikiSearchTerm = "Anthony Blunt"
wikiPage = wikipedia.page(wikiSearchTerm)
wikiTitle = wikiPage.title.encode('utf-8')
wikiPageID = wikiPage.pageid.encode('utf-8')
wikiURL = wikiPage.url.encode('utf-8')
wikiSummary = wikiPage.summary.encode('utf-8')
wikiCategories = encodeList(wikiPage.categories)
wikiReferences = encodeList(wikiPage.references)
wikiImageLinks = encodeList(wikiPage.images)
wikiLinks = encodeList(wikiPage.links)
wikiContent = wikiPage.content.encode('utf-8')
# print wikiTitle
# print wikiPageID
# print wikiURL
# print wikiSummary
# print wikiCategories
# print wikiReferences
# print wikiImageLinks
# print wikiLinks
# print wikiContent
WikiDict = createDict(wikiPage)
writeContentTextFile(wikiPage)
writeLinksTextFile(wikiPage)
# linkstext = readLinksTextFile(wikiPage)
# print linkstext
writeJsonFile(WikiDict)
# jsondict = readJsonFile(WikiDict)
# print jsondict
writeCsvFile(WikiDict)
# csvdict = readCsvFile(WikiDict)
# print csvdict
wikiLinks =['Bletchley Park', 'Boris Bykov', 'Boris Morros', 'Bournemouth', 'Brian Sewell', 'British Empire', 'British Library', 'British Museum', 'Cambridge Apostles', 'Cambridge Five', 'Cambridge Spies', 'Canada', 'Charles Higham (biographer)', 'Christopher John Boyce', 'Claude Bowes-Lyon, 14th Earl of Strathmore and Kinghorne', 'Clayton J. Lonetree', 'Communist Party of Great Britain', 'Courtauld Institute of Art', 'Cubism', 'Curator', 'Daily Mail Online', 'Dave Springhall', 'David Crook', 'David Greenglass', 'David Sheldon Boone', 'Denis Mahon', 'Dick White', 'Dieter Gerhardt', 'Digital object identifier', 'Donald Hiss', 'Donald Maclean (spy)', 'Duke of Windsor', 'Dunkirk', 'E. M. Forster', 'Earl Edwin Pitts', 'Edith Tudor Hart', 'Edward Croft-Murray', 'Edward Lee Howard', 'Elizabeth Bentley', 'Elizabeth Bowes-Lyon', 'Elizabeth II', 'Elizabeth II of the United Kingdom', 'England', 'Enigma (machine)', 'Espionage', 'Ethel Gee', 'Eug\xc3\xa8ne Delacroix', 'Evening Standard', 'Festschrift', 'Find a Grave', 'First class degree', 'Fitzwilliam Museum', 'Flora Wovschin', 'Francis Haskell', 'Fred Rose (politician)', 'French Baroque', 'Fyodor Raskolnikov', 'Geoffrey Palmer (actor)', 'Geoffrey Prime', 'George Blake', 'George Koval', 'George Trofimoff', 'George VI', 'Gerda Munsinger', 'Goronwy Rees', 'Graham Shepard', 'Guy Burgess', 'Hampshire', 'Hansard', 'Harold Glasser', 'Harold James Nicholson', 'Harold Ware', 'Harry Dexter White', 'Harry Gold', 'Harry Houghton', 'Harvard University', 'Hede Massing', 'Herman Simm', 'Hirohide Ishida', 'History of Art', 'History of Soviet and Russian espionage in the United States', 'Hotsumi Ozaki', 'House of Commons of the United Kingdom', 'Ian Fleming', 'Ian Richardson', 'Ignace Reiss', 'Igor Gouzenko', 'Illegals Program', 'Integrated Authority File', 'International Standard Book Number', 'International Standard Name Identifier', 'International Standard Serial Number', 'Isaiah Oggins', 'J. Peters', 'JSTOR', 'Jack Dunlap', 'Jack Soble', 'James Bond', 'James Fox', 'James Hall III', 'Jane Turner', 'Japan', 'Jerry Whitworth', 'Jim Skardon', 'Joel Barr', 'John Abt', 'John Alexander Symonds', 'John Anthony Walker (spy)', 'John Banville', 'John Betjeman', 'John Cairncross', 'John Edward Bowle', 'John Herrmann', 'John Peet (1915\xe2\x80\x931988)', 'John Pope-Hennessy', 'John Schlesinger', 'John Shearman', 'John Summerson', 'John Vassall', 'John White (art historian)', 'Jonathan Petropoulos', 'Joseph Losey', 'Judith Coplon', 'Julian Wadleigh', 'Julius and Ethel Rosenberg', 'Karl Koecher', 'Kenneth Clark', 'Kim Philby', 'King George VI', 'King\xe2\x80\x99s College, Cambridge', 'Klaus Fuchs', 'Knight', 'Knight Commander of the Royal Victorian Order', 'Konon Molody', 'Kriegsmarine', 'Lee Johnson (Art Historian)', 'Lee Pressman', 'Library of Congress Control Number', 'Litzi Friedmann', 'Lona Cohen', 'London, UK', 'London Evening Standard', 'Louis MacNeice', 'Louvre', 'MI5', 'MI6', 'Madras', 'Malcolm Muggeridge', 'Mannerism', 'Margaret Thatcher', 'Maria Wicher', 'Marlborough College', 'Marxism', 'Mata Hari', 'McCarthyism', 'Melita Norwood', 'Melvin Day', 'Michael Adeane, Baron Adeane', 'Michael Bettaney', 'Michael Jaff\xc3\xa9', 'Michael John Smith (espionage)', 'Michael Kitson', 'Michael Straight', 'Michael Whitney Straight', 'Michael Williams (actor)', 'Mihail Gorin', 'Miranda Carter', 'Morris Cohen (Soviet spy)', 'Morris Cohen (spy)', 'Morton Sobell', 'Moura Budberg', 'Myra Soble', 'NKVD', 'Nathan Witt', 'Nathaniel Weyl', 'National Art Gallery of New Zealand', 'National Gallery of Art', 'Neil Macgregor', 'Newsnight', 'Nicholas Penny', 'Nicholas Serota', 'Nicolas Poussin', 'Nigel West', 'Noel Annan', 'Noel Field', 'Numismatist', 'OCLC', 'Official secret', 'Oliver Millar', 'Oliver Millar (art historian)', 'Owen Morshead', 'Oxford Dictionary of National Biography', 'Pablo Picasso', 'Peter Hennessy', 'Peter Lasko', 'Peter Wright', 'Phoney war', 'Pietro da Cortona', 'Portland Spy Ring', 'Pre-Raphaelites', 'Princess Marina of Greece and Denmark', 'Private Eye', 'Prunella Scales', 'Queen Elizabeth II', 'Queen Mother', 'Reino H\xc3\xa4yh\xc3\xa4nen', 'Renaissance', 'Reyner Banham', 'Richard Miller (agent)', 'Richard Sorge', 'Robert Hanssen', 'Robert Lee Johnson (spy)', 'Robert Soblen', 'Robert Thompson (Soviet spy)', 'Roman \xc3\xa0 clef', 'Ron Bloore', 'Ronald Pelton', 'Rothschild', 'Roy Jenkins', 'Royal Academy', 'Royal Archives', 'Royal Librarian', 'Royal Library, Windsor', 'Royal Navy', 'Royal Victorian Order', 'Rubens', 'Rudolf Abel', 'Ryuzo Sejima', 'Sam Carr', 'Samuel West', 'Sanzo Nosaka', 'Saville Sax', 'Schlosshotel Kronberg', 'Sicilian Baroque', 'Sicily', 'Sir Alan Lascelles', 'Slade Professor of Fine Art', 'Southampton', 'Soviet Union', 'Spy', "Surveyor of the Queen's Pictures", 'Syst\xc3\xa8me universitaire de documentation', 'T. S. R. Boase', 'Tate Gallery', 'Telegraph Media Group', 'The Daily Mail', 'The Daily Telegraph', 'The Dictionary of Art', 'The Guardian', 'The London Review of Books', 'The Observer', 'The Untouchable (novel)', 'Theodore Hall', 'Third World War', 'Thomas Hinde (novelist)', 'Thomas Patrick Cavanaugh', 'Toronto', 'Travellers Club', 'Trinity College, Cambridge', 'Tripos', 'UK', 'Ultra', 'Union List of Artist Names', 'United Kingdom', 'University don', 'University of London', 'Van Dyck', 'Venona project', 'Victor Perlo', 'Victor Rothschild', 'Victoria, Princess Royal', 'Vincent Reno', 'Virtual International Authority File', 'Vitaly Shlykov', 'Vladimir Mikhaylovich Petrov (diplomat)', 'Walter Krivitsky', 'Ward Pigman', 'Wehrmacht', 'Westminster', 'Whittaker Chambers', 'Wilfrid Jasper Walter Blunt', 'Wilfrid Scawen Blunt', 'Wilhelm II, German Emperor', 'William Blake', 'William Malisoff', 'William Perl']
for each in wikiLinks:
	wikiSearchTerm = each
	wikiPage = wikipedia.page(wikiSearchTerm)
	WikiDict = createDict(wikiPage)
	writeContentTextFile(wikiPage)
	writeLinksTextFile(wikiPage)
	writeJsonFile(WikiDict)
