#!/usr/bin/python3.2
print("Content-Type: text/html\n\n")

import cgi
import cgitb

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
                  <li><a href="../DemocraticPlaylists/login.html">Log In</a></li>
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

  resultsList.append(song1)
  resultsList.append(song2)
  resultsList.append(song3)

  return resultsList


def main():

  # stores total vote counts
  results = []

  songNames = [ "Drake - God's Plan", 
                "Dua Lipa - IDGAF:", 
                "Ariana Grande - No Tears Left to Cry"
              ]

  results = readResults(results)

  print("<h2>", songNames[0], ":", results[0], " votes</h2>")
  print("<h2>", songNames[1], ":", results[1], " votes</h2>")
  print("<h2>", songNames[2], ":", results[2], " votes</h2>")

  iFrame = '<iframe id = "theVideo" width="44%" height="200" src="'
  iFrame += 'https://www.youtube.com/embed?listType=search&list='
  iFrame += songNames[results.index(max(results))]
  iFrame += '" frameborder="0" style="border: solid 4px #37474F"></iframe>'


  print(iFrame)


  

htmlHead()
main()
htmlTail()
