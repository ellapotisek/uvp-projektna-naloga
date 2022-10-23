<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#ffffff">
    <title>Login</title>
    <link rel="stylesheet" href="/static/main.css">
  </head>
  <body>
  	<h2>Prijava</h2>
  	<form method='post' action='/login' enctype='multipart/form-data'>
  		<input type='text' name='username'>
  		<input type='text' name='password'>
  		<input type='submit' value='Submit'>
  	</form>
  </body>
</html>
