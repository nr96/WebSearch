import requests


def main():
	splitTxt = [] # list to hold parsed txt from webpage
	keyHist = [] # list to hold keyword history
	page = '' # var to hold webpage url

	page = getWebpage(page) # get webpage url and store in page
	txt = parseWebpage(page) # parse webpage content into txt
	splitTxt = splitPage(txt, splitTxt) # split webpage txt from str to list
	keywordSearch(txt, page, keyHist) # search txt for keyword

	while True: # continuosly ask until user wants to quit
		getChoice(txt, page, keyHist) # ask user what they wish to do next


def splitPage(txt, splitTxt):
	splitTxt = txt.split('<') # split txt using '<' as delimeter
	return splitTxt # return list to main function


def getChoice(txt, page, keyHist):
	print("\nDo you wish to 1) enter a new webpage 2) enter a new keyword 3) exit")
	choice = input("Please enter '1','2', or '3': ") # get choice from user
	if choice == '1':
		getWebpage() # user wishes to search new webpage
		keywordSearch(txt, page, keyHist) # get new keyword from user
	if choice == '2':
		keywordSearch(txt, page, keyHist) # user wishes to enter new keyword on same webpage
	if choice == '3':
		print("exiting program...") # user wishes to exit program
		exit()


def getKeywordCount(txt,key):
	txt = txt.upper() # eliminate str casing variability for ease of counting
	count = txt.count(key.upper()) # search txt for keyword
	return count


def keywordSearch(txt, page, keyHist):
	key = input("Please enter a keyword to search for: ") # get keyword from user
	keyHist.append(key)
	count = getKeywordCount(txt,key) # get count from txt
	print("Keyword '" + key + "' appears " + str(count) + " times in " + str(page))


def getWebpage(page):
	page = input("Please enter a webpage url: ") # get url from user
	while "https://" not in page: # make sure a complete url is entered
		page = input("Please enter complete url i.e 'https://...' : ")
	return page


def parseWebpage(page):
	#page = getWebpage(page)
	response = requests.get(page) # get info from webpage
	txt = response.text # turn webpage content into text
	return txt


main()
