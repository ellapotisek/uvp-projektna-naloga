<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#ffffff">
    <title>Naredi nalogo</title>
    <link rel="stylesheet" href="/static/main.css">
  </head>
  <body>
  	Naloži eno datoteko z vsebino (.txt), datoteke z vhodnimi podatki (1.in, 2.in, ...) in z rešitvami (1.out, 2.out, ...).
    <form method='post' action='/create_problem/upload' enctype='multipart/form-data'>
    	<input type='text' name='title'><br>
    	<input type='file' name='content'><br>
    	<input type='file' name='input' multiple><br>
    	<input type='file' name='output' multiple><br>
    	<a href=/{{id}}><input type='submit' value='Submit'></a>
	</form>
          
  </body>
</html>
