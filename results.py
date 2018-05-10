#!/usr/bin/python3.2
print("Content-Type: text/html\n\n")

import cgi
import cgitb

import scrape

def htmlHead():
	print(""" 
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="favicon.ico">

    <title>Democratic Playlists</title>

    <!-- Bootstrap core CSS -->
    <link href="../DemocraticPlaylists/css/bootstrap.min.css" rel="stylesheet">

    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <link href="../DemocraticPlaylists/css/ie10-viewport-bug-workaround.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="../DemocraticPlaylists/cover.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="../DemocraticPlaylists/js/ie-emulation-modes-warning.js"></script>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
    <link href="https://fonts.googleapis.com/css?family=Anton|Indie+Flower|Jua" rel="stylesheet">
  </head>

  <body>

    <div class="site-wrapper">

      <div class="site-wrapper-inner">

        <div class="cover-container">

          <div class="masthead clearfix">
            <div class="inner">
              <h3 class="masthead-brand">Democratic Playlists</h3>
              <nav>
                <ul class="nav masthead-nav">
                  <li><a href="../DemocraticPlaylists/index.html">Home</a></li>
                  <li><a href="../DemocraticPlaylists/register.html">Register</a></li>
                  <li class = "active"> <a href="#">Currently Playing...</a></li>
                  <li><a href="../DemocraticPlaylists/about.html">About</a></li>
                </ul>
              </nav>
            </div>
          </div>

          <div class="inner cover">
""")


def htmlTail():
	print(""" 
		  <div class="mastfoot">
            <div class="inner">
              <p>Lucas Futch | Kevin Long Noll | <a class = "myLink" href = "https://www.phostell.com/wp-content/uploads/2018/01/Bridge-Brooklyn-Bridge-Buildings-City-City-Lights-Dark-Evening-Lights-New-York-City-Night-Nyc-Ocean-Reflection-River-Sea-Sky-Skyline-Skyscrapers-Tall-Tower-United-States-Of-America-Urban-Water.jpeg">Image Source</a> </p>
            </div>
          </div>

        </div>

      </div>

    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>
    <script src="../DemocraticPlaylists/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="../DemocraticPlaylists/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>
""")

def saveResults(name):
  results = open("results.txt", 'a')
  results.write(name + "\n")
  results.close()

def readResults(resultsList):
  results = open("results.txt", 'r')

  for line in results:
    resultsList.append(line.rstrip('\n').lstrip())

  results.close()
  
  return resultsList

def readSongs(mySongs):
    songFile = open("songs.txt", "r")
    for line in songFile:
        mySongs.append(line.rstrip('\n'))

    songFile.close()
    return mySongs

def addVote():
  data = cgi.FieldStorage()

  if "song" not in data:
    print("<h1 style = 'margin-bottom:40px;'>No vote was cast!</h1>")
  else:
    saveResults(data['song'].value)

def results():

  # stores total vote counts
  results = []
  songNames = []

  songNames = readSongs(songNames)

  splitSongsName = []
  splitSongsURL = []

  for item in songNames:
    name, url = item.split(":")
    splitSongsName.append(name)
    splitSongsURL.append(url)

  results = readResults(results)

  listname1 = []
  listname2 = []
  listname3 = []

  for items in results:
    name, vote = items.split(":")
    if vote == "1":
      listname1.append(name)
    if vote == "2":
      listname2.append(name)
    if vote == "3":
      listname3.append(name)

  numvotessong1 = len(listname1)
  numvotessong2 = len(listname2)
  numvotessong3 = len(listname3)

  popularsong = [numvotessong1, numvotessong2, numvotessong3]

  print("<h2>", splitSongsName[0], ":", numvotessong1, " votes</h2>")
  print("<h2>", splitSongsName[1], ":", numvotessong2, " votes</h2>")
  print("<h2>", splitSongsName[2], ":", numvotessong3, " votes</h2>")

  iFrame = '<iframe id = "theVideo" width="44%" height="200" src="'
  iFrame += 'https://www.youtube.com/embed?listType=search&list='
  iFrame += splitSongsURL[popularsong.index(max(popularsong))]
  iFrame += '" frameborder="0" style="border: solid 4px #37474F"></iframe>'

  if len(results) == 10:
    open("results.txt", "w").close()
    scrape.scrape()



  print(iFrame)


if __name__ == '__main__':
    htmlHead()
    addVote()
    results()
    htmlTail()
