#!/usr/bin/python3.2
print("Content-Type: text/html\n\n")

import cgi
import cgitb

def htmlHead():
	print("<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'><meta http-equiv='X-UA-Compatible' content='IE=edge'><meta name='viewport' content='width=device-width, initial-scale=1'><meta name='description' content=''><meta name='author' content=''><link rel='icon' href='favicon.ico'><title>Democratic Playlists</title><link href='../DemocraticPlaylists/css/bootstrap.min.css' rel='stylesheet'><link href='../DemocraticPlaylists/css/ie10-viewport-bug-workaround.css' rel='stylesheet'><link href='../DemocraticPlaylists/cover.css' rel='stylesheet'><script src='../DemocraticPlaylists/js/ie-emulation-modes-warning.js'></script><script src='https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js'></script><script src='https://oss.maxcdn.com/respond/1.4.2/respond.min.js'></script><link href='https://fonts.googleapis.com/css?family=Anton|Indie+Flower|Jua' rel='stylesheet'></head><body><div class='site-wrapper'><div class='site-wrapper-inner'><div class='cover-container'><div class='masthead clearfix'><div class='inner'><h3 class='masthead-brand'>Democratic Playlists</h3><nav><ul class='nav masthead-nav'><li><a href='../DemocraticPlaylists/index.html'>Home</a></li><li class='active'><a href='#'>Currently Playing...</a></li><li><a href='../DemocraticPlaylists/about.html'>About</a></li></ul></nav></div></div><div class='inner cover'>")

def htmlTail():
	print("<div class='mastfoot'><div class='inner'><p>Lucas Futch | Kevin Long Noll | <a href = 'https://www.bigbustours.com/en/new-york/top-10-things-to-do-in-new-york/'>Image Source</a> </p></div></div></div></div></div><script src='https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js'></script><script>window.jQuery || document.write('<script src='../DemocraticPlaylists/js/vendor/jquery.min.js'><\/script>')</script><script src='../DemocraticPlaylists/js/bootstrap.min.js'></script><script src='../DemocraticPlaylists/js/ie10-viewport-bug-workaround.js'></script></body></html>")

# save the computed results
def saveResults(name):
	results = open("results.txt", 'a')
	results.write(name + "\n")
	results.close()

# get grades from file
def readResults(resultsList):
	grades = open("results.txt", 'r')

	song1 = 0
	song2 = 0
	song3 = 0

	for line in grades:
		song = line.rstrip('\n')
		if song == "song1":
			song1 += 1
		elif song == "song2":
			song2 += 1
		elif song == "song3":
			song3 += 1
	
	grades.close()

	return song1, song2, song3

def main():

	results = []
	song1 = 0
	song2 = 0
	song3 = 0

	
	form = cgi.FieldStorage()

	if "song" not in form:
		print("<h1>Please select a song!</h1>")
	else:
		songSelection = form['song'].value
		saveResults(songSelection)


	song1, song2, song3 = readResults(results)

	print("<h2>Song 1 Votes:", song1, "</h2>")
	print("<h2>Song 2 Votes:", song2, "</h2>")
	print("<h2>Song 3 Votes:", song3, "</h2>")


htmlHead()
main()
htmlTail()
