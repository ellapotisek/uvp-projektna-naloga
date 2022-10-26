<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#ffffff">
    <title>Problems list</title>
    <link rel="stylesheet" href="/main.css">
  </head>
  <body>
  	<nav>
	   <ul class="navul">
	      <li class="strani"><a href="/" class="active">Seznam nalog</a></li>
	   % if username == None:
  			<li class="prijava"><a href="/login">Prijava</a></li>
  			<li class="prijava"><a href="/new_user">Nov uporabnik</a></li>
  		% else:
  			<li class="navtext">Prijavljen kot {{username}}.</li>
  			<li class="prijava"><a href="/logout">Odjava</a></li>
  		% end
  		</ul>
   </nav>
  	<h2>Seznam nalog</h2>
  	<ol>
  	% for id, problem in enumerate(problems):
  		<li><a href="/{{id}}" class="naloga">{{problem.title}}</a></li>
  	% end
  	</ol>
  	<br>
  	<a href="/create_problem">Nova naloga</a>
  	<br>
  		
  </body>
</html>
