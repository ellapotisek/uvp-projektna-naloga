<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#ffffff">
    <title>{{problem.title}}</title>
    <link rel="stylesheet" href="/static/main.css">
  </head>
  <body>
  	<h2>{{problem.title}}</h2>
    {{problem.content}}
    <form method='post' action='/{{id}}/upload' enctype='multipart/form-data'>
    	<input type='file' name='file'>
    	<input type='submit' value='Submit'><br>
	</form>
    <a href="/{{id}}/submissions">Oddaje</a>
  </body>
</html>
