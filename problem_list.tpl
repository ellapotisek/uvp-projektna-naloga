<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#ffffff">
    <title>Problems list</title>
    <link rel="stylesheet" href="/static/main.css">
  </head>
  <body>
  	<h2>List of Problems</h2>
  	% for id, problem in enumerate(problems):
  		<a href="/{{id}}">{{problem.title}}</a><br>
  	% end
  </body>
</html>
