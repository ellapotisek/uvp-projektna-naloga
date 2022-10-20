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
  	<br>
  	<a href="/create_problem">Nova naloga</a>
  	<br>
  	% if username == None:
  		<a href="/login">Prijava</a><br>
  		<a href="/new_user">Nov uporabnik</a>
  	% else:
  		Prijavljen kot {{username}}. <a href="/logout">Odjava</a>
  	% end
  		
  </body>
</html>
