#!/usr/bin/python3.2
import urllib.request
import random
import unidecode

def saveResults(name):
  results = open("allSongs.txt", 'a')
  results.write(name + "\n")
  results.close()

# function to get word from the web by scraping
def scrape():
  #open text file from web (issue a request), scrape data and put it into a list called animals
  website = urllib.request.urlopen('http://kworb.net/youtube/')
  website = website.read().decode("utf-8")

  songList = []


  # get the first part of the website
  before = 0
  after = 4000
  currentString = website[before:after]

  # get top 50 songs
  for item in range(475):
  	# find the first video link and save it
  	codeStart 	= currentString.find("video/")
  	code 		= currentString[codeStart + 6 : codeStart + 17]
  	
  	# song name comes after video link
  	songNameString = currentString[codeStart + 24 : codeStart + 80]

  	# find item to end song name, and make sure its not a minimum value for min() function
  	songNameEndA = songNameString.find("<")
  	songNameEndB = songNameString.find("(")
  	songNameEndC = songNameString.find("|")

  	if songNameEndA == -1:
  		songNameEndA = 100
  	if songNameEndB == -1:
  		songNameEndB = 100
  	if songNameEndC == -1:
  		songNameEndC = 100

  	# smallest value is used to fetch entire song name
  	songNameEnd = min(songNameEndA, songNameEndB, songNameEndC)
  	songName = songNameString[0: songNameEnd]

  	songName = unidecode.unidecode(songName)

  	# save song and youtube code
  	saveResults(songName + ":" + code)

  	# before is now in front of wherever the code was found
  	before = before + codeStart + 25
  	# after is adding more characters to the string
  	after = before + 1000
  	# create new string with further website parts
  	currentString = website[before:after]

  # select and save three songs
  # open("songs.txt", "w").close()
  # for song in range(3):
  # 	random.choice(songList)
  # 	saveResults(random.choice(songList))

if __name__ == '__main__':
    scrape()
