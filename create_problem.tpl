<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#ffffff">
    <title>Naredi nalogo</title>
    <link rel="stylesheet" href="/main.css">
  </head>
  <body>
     <nav>
	   <ul class="navul">
	      <li class="strani"><a href="/">Seznam nalog</a></li>
	   % if username == None:
  	      <li class="prijava"><a href="/login">Prijava</a></li>
  		  <li class="prijava"><a href="/new_user">Nov uporabnik</a></li>
  		% else:
  		  <li class="navtext">Prijavljen kot {{username}}.</li>
  		  <li class="prijava"><a href="/logout">Odjava</a></li>
  		% end
  		</ul>
   	  </nav>
  	<p>Naloži eno datoteko z vsebino (.txt), datoteke z vhodnimi podatki (1.in, 2.in, ...) in z rešitvami (1.out, 2.out, ...).</p>
    <form method='post' action='/create_problem/upload' enctype='multipart/form-data'>
    	<table>
    		<tr>
    			<th>Naslov</th>
    			<th><input type='text' name='title'></th>
    		</tr>
    		<tr>
    			<th>Časovna omejitev</th>
    			<th><input type='text' name='time_limit'></th>
    		</tr>
    		<tr>
    			<th>Vsebina naloge</th>
    			<th><input type='file' name='content'></th>
    		</tr>
    		<tr>
    			<th>Datoteke z vhodnimi podatki</th>
    			<th><input type='file' name='input' multiple></th>
    		</tr>
    		<tr>
    			<th>Datoteke z rešitvami</th>
    			<th><input type='file' name='output' multiple></th>
    		</tr>
    	</table>
    	<input type='submit' value='Submit'>
	</form>
          
  </body>
</html>
