#!/usr/bin/python
#-*- coding: utf-8 -*- 

import os
# import urllib2
from bs4 import BeautifulSoup

class Sefer(object):
	""""""
	def __init__(self, seferTitle = "None", seferNumber = 0):
		self.seferTitle = seferTitle
		self.seferNumber = seferNumber
		base_directory = "C:\Users\\nassan\Downloads\\tanach_htmls\\books_of_chumash\\"
		sefarim_array = os.listdir(base_directory)
		self.souped = BeautifulSoup(open(base_directory + sefarim_array[seferNumber-1]))

	def getPerakim(self):
		"""Returns a list of <table> tags that represent Perakim"""
		return self.souped.findAll("table")

		
class Pasuk(object):
	"""This class contains the Metadata of a pasuk, and its contents as a unicode string"""

	def __init__(self, seferTitle = "Sefer", perekNumber = 0, pasukNumber = 0, Parsha = "Parsha", Aliyah = "None", contents = "None"):
		self.sefer = seferTitle
		self.perek = perekNumber
		self.pasukNumber = pasukNumber
		self.parsha = Parsha
		self.aliyah = Aliyah
		self.contents = contents


def createPasukim(perek, perekNumber = 0, sefer = "None"):
	"""Takes a BeautifulSoup <table> tag and returns an array of Pasuk objects"""
	trTagsList = perek.findAll("tr")
	pasukimInPerek = []
	pasukNumber = 1
	for trTag in trTagsList:
		# This try accounts for the big letter at the beginning of Sefer that is 
		# seperated from the rest of the Pasuk
		currentPasuk = Pasuk("Beresheis",perekNumber,pasukNumber)
		try:
			currentPasuk.contents = repr(trTag.td.big.string + trTag.td.contents[-1] )
		except:
			currentPasuk.contents = repr(trTag.td.contents[-1])
		pasukimInPerek.append(currentPasuk)
		pasukNumber += 1

	return pasukimInPerek















beresheis = Sefer("Beresheis",1)
perek_list = beresheis.getPerakim()
perekNumber = 1
arrayOfPerakim = []
for perek in perek_list:
	# createPasukim returns an array of Pasuk objects
	arrayOfPerakim.append(createPasukim(perek, perekNumber,"Beresheis"))
	perekNumber += 1
# print repr(perek_list[0].tr.nextSibling.td.contents[-1])

arrayOfAllPasukim = []
primaryKey = 1
for eachperek in  arrayOfPerakim:
	for eachpasuk in eachperek:
		# Create tuple containg all pasuk object attributes as members of the tuple
		pasukAttributesArray = [primaryKey,eachpasuk.sefer,eachpasuk.perek,eachpasuk.pasukNumber,eachpasuk.parsha,eachpasuk.aliyah,repr(eachpasuk.contents)]
		arrayOfAllPasukim.append(pasukAttributesArray)
		primaryKey+=1
# print len(arrayOfAllPasukim)

# print arrayOfAllPasukim[500][6]

import sqlite3 as lite
import sys

dbConnection = lite.connect("chumash.db")
# dbConnection.text_factory = str

with dbConnection:
	cursor = dbConnection.cursor()
	cursor.execute("DROP TABLE IF EXISTS pasukimInBeresheis")
	cursor.execute("CREATE TABLE pasukimInBeresheis(Id INTEGER PRIMARY KEY, seferTitle TEXT, perekNumber INT, pasukNumber INT, parsha TEXT, aliyah TEXT, contents TEXT)")
	# for currentPasuk in arrayOfAllPasukim:
	for x in xrange(0,len(arrayOfAllPasukim)):
		cursor.execute("INSERT INTO pasukimInBeresheis VALUES(?,?,?,?,?,?,?)", arrayOfAllPasukim[x])

print beresheis.souped.table.tr.td.contents[-1].encode('windows-1255', 'ignore')




