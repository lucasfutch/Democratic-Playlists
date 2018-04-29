#!/usr/bin/python3.2
print("Content-Type: text/html\n\n")

import cgi
import cgitb

def htmlHead():
	print("<!DOCTYPE HTML><html><head><title>Playing Song</title><link rel='stylesheet' type='text/css' href='../offcanvas.css'></head><body>")	

def htmlTail():
	print("</body></html>")

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

	print("<h1>Song 1 Votes:", song1, "</h1>")
	print("<h1>Song 2 Votes:", song2, "</h1>")
	print("<h1>Song 3 Votes:", song3, "</h1>")


htmlHead()
main()
htmlTail()
