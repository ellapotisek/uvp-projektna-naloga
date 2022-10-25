<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#ffffff">
    <title>Nov uporabnik</title>
    <link rel="stylesheet" href="/main.css">
  </head>
  <body>
     <nav>
	   <ul class="navul">
	      <li class="strani"><a href="/">Seznam nalog</a></li>
  	   </ul>
   	  </nav>
    <form method='post' action='/new_user' enctype='multipart/form-data'>
    	<table>
    		<tr>
    			<th>Uporabniško ime</th>
    			<th><input type='text' name='username'></th>
    		</tr>
    		<tr>
    			<th>Geslo</th>
    			<th><input type='text' name='password'></th>
    		<tr>
    		</tr>
    			<th>Potrditev gesla</th>
    			<th><input type='text' name='confirm_password'></th>
    		</tr>
    	</table>
    	<input type='submit' value='Submit'>
	</form>
          
  </body>
</html>
