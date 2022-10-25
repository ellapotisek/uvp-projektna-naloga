<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#ffffff">
    <title>{{problem.title}}</title>
    <link rel="stylesheet" href="/main.css">
  </head>
  <body>
  	<nav>
	   <ul class="navul">
	      <li class="strani"><a href="/">Seznam nalog</a></li>
	      <li class="strani"><a href="/{{id}}" class="active">{{problem.title}}</a></li>
	   % if username == None:
  		  <li class="prijava"><a href="/login">Prijava</a></li>
  		  <li class="prijava"><a href="/new_user">Nov uporabnik</a></li>
  		% else:
  		  <li class="navtext">Prijavljen kot {{username}}.</li>
  		  <li class="prijava"><a href="/logout">Odjava</a></li>
  		% end
  		</ul>
   	</nav>
  	<h2>{{problem.title}}</h2>
    {{problem.content}}
    <form method='post' action='/{{id}}/upload' enctype='multipart/form-data'>
    	<input type='file' name='file'>
    	<input type='submit' value='Submit'><br>
	</form>
    <a href="/{{id}}/submissions">Oddaje</a>
  </body>
</html>
