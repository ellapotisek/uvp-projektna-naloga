<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#ffffff">
    <title>Nov uporabnik</title>
    <link rel="stylesheet" href="/static/main.css">
  </head>
  <body>
    <form method='post' action='/new_user' enctype='multipart/form-data'>
    	<input type='text' name='username'><br>
    	<input type='text' name='password'><br>
    	<input type='text' name='confirm_password'><br>
    	<input type='submit' value='Submit'>
	</form>
          
  </body>
</html>
