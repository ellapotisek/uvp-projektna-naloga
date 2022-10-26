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
  	<p>Naloži eno datoteko z vsebino (.txt), datoteke z vhodnimi podatki (1.in, 2.in, ...) in z rešitvami (1.out, 2.out, ...). Časovna omejitev je v sekundah.</p>
    <form method='post' action='/create_problem/upload' enctype='multipart/form-data'>
    	<table>
    		<tr>
    			<td>Naslov</td>
    			<td><input type='text' name='title'></td>
    		</tr>
    		<tr>
    			<td>Časovna omejitev</td>
    			<td><input type='text' name='time_limit'></td>
    		</tr>
    		<tr>
    			<td>Vsebina naloge</td>
    			<td><input type='file' name='content'></td>
    		</tr>
    		<tr>
    			<td>Datoteke z vhodnimi podatki</td>
    			<td><input type='file' name='input' multiple></td>
    		</tr>
    		<tr>
    			<td>Datoteke z rešitvami</td>
    			<td><input type='file' name='output' multiple></td>
    		</tr>
    	</table>
    	<input type='submit' value='Submit'>
	</form>
          
  </body>
</html>
