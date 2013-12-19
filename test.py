from BeautifulSoup import BeautifulSoup																																																												
path = "/home/nassan/pasukim/tanach_htmls/t/t0101.htm"
soup = BeautifulSoup(open(path))
pArray = soup.findAll("p")
pasukimBTags = pArray[1].findAll("b")
# print len(pasukimBTags)
pasukimArray = []
for bTag in pasukimBTags:
	if(bTag == pasukimBTags[0]):
		tag = bTag.nextSibling.nextSibling
		pasukimArray.append(tag.string + tag.nextSibling)
	else:
		pasukimArray.append(bTag.nextSibling)

for pasuk in pasukimArray:
	print pasuk