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
                  <li class = "active"><a href="../DemocraticPlaylists/index.html">Home</a></li>
                  <li><a href="../DemocraticPlaylists/register.html">Register</a></li>
                  <li><a href="../cgi-bin/currentlyPlaying.py">Currently Playing...</a></li>
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

def printLogin():
    print(""" 
<h2>Login</h2>
          
          <!-- This is the buttons for song selections -->
            <div class="btn-group" role="group" aria-label="...">


              <form action = "../cgi-bin/login.py" method = "post" id = "loginForm">
                <!-- <button type="button" class="btn btn-default">Song 1</button>
                <button type="button" class="btn btn-default">Song 2</button>
                <button type="button" class="btn btn-default">Song 3</button> -->

                <p class = "formText">Username</p>
                <input class = "form" type="text" name="username" placeholder = "username">
                <p class = "formText">Password</p>
                <input class = "form" type="password" name="password" placeholder = "password"><p>

                <input class = "form"  type = "submit" name = "submit" value = "Log In">
                <input class = "form"  type="reset" name="cancel" value=cancel>


              </form>


            </div>



""")

def printVote(username, songList):
  print("""
<h2>Vote for your Song:</h2>
          
          <!-- This is the buttons for song selections -->
            <div class="btn-group" role="group" aria-label="...">


              <form action = "../cgi-bin/results.py" method = "post" id = "nameForm">

                <input type = "radio" name = "song" value = " """ + username + """:1"><p>""" + songList[0] + """</p>""" + 
                """<input type = "radio" name = "song" value = " """ + username + """:2"><p>""" + songList[1] + """</p>""" +
                """<input type = "radio" name = "song" value = "  """ + username + """:3"><p>""" + songList[2] + """</p>
                <input class = "form" type = "submit" value = "Enter">
              </form>
            </div>
    """)

def readUsers(myUser):
    users = open("users.txt", 'r')
    found = False
  
    for line in users:
        user = line.rstrip('\n')
        username, password = user.split(':')

        if (myUser == username):
            found = True

    users.close()
    return found

def readSongs(mySongs):
    songFile = open("songs.txt", 'r')

    for line in songFile:
      mySongs.append(line.rstrip('\n'))

    songFile.close()
    return mySongs


def main():
    songs = []
    splitSongs = []
    
    data = cgi.FieldStorage()
    songs = readSongs(songs)

    for item in songs:
      name, url = item.split(":")
      splitSongs.append(name)

    if "username" not in data and "password" not in data:
        print("<h2>Please fill in all fields!</h2>")
        printLogin()
    else: 
        username = data["username"].value
        password = data["password"].value

        exists = readUsers(username)
        if exists:
            print("<h2>Welcome " + username + "!</h2>")
            printVote(username, splitSongs)
        else:
            print("<h2>Username or password are incorrect!</h2>")
            printLogin()


htmlHead()
main()
htmlTail()