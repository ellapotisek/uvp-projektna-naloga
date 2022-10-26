<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#ffffff">
    <title>Oddaja</title>
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
	<p>Naloga uspešno oddana.</p>
	<table>
	% for i, res in enumerate(results):
		<tr>
			<td>{{i+1}}</td>
			<td>{{res}}</td>
		</tr>
	% end
	</table>
  </body>
</html>
