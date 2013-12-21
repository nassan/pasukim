# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup																																																												
path = "/home/nassan/pasukim/tanach_htmls/t/t0101.htm"
soup = BeautifulSoup(open(path))
pArray = soup.findAll("p")
pasukimBTags = pArray[1].findAll("b")

pasukimArray = []
for bTag in pasukimBTags:
	if(bTag == pasukimBTags[0]):
		tag = bTag.nextSibling.nextSibling
		pasukimArray.append(unicode(tag.string + tag.nextSibling))
	else:
		pasukimArray.append(unicode(bTag.nextSibling))

# Remove {פ} Torah paragraph breaks from each pasuk if it has it
filterPasukimArray=[]
for pasuk in pasukimArray:
	filterPasukimArray.append(pasuk.replace(u"{פ}",""))

# Decare an array where each index holds a dictionary of pasuk details and contents:
pasukDictionaries = []
pasukNumber = 1

for bTag, pasuk in zip(pasukimBTags,filterPasukimArray):
	pasukDetails = dict(seferTitle = "בראשית",perekNumber = 1,pasukNumber = pasukNumber,pasukName = bTag.string, parshaName = "בראשית",aliyahName ="none_yet",contents = pasuk)
	pasukDictionaries.append(pasukDetails)
	pasukNumber += 1

import json
f = open("app/perek1.json","wb")
json.dump(pasukDictionaries,f)
f.close()
