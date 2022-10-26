<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#ffffff">
    <title>Login</title>
    <link rel="stylesheet" href="/main.css">
  </head>
  <body>
     <nav>
	   <ul class="navul">
	      <li class="strani"><a href="/">Seznam nalog</a></li>
  	   </ul>
   	  </nav>
  	<h2>Prijava</h2>
  	<form method='post' action='/login' enctype='multipart/form-data'>
  		<table>
  			<tr>
  				<td>Uporabniško ime</td>
  				<td><input type='text' name='username'></td>
  			<tr>
  			</tr>
  				<td>Geslo</td>
  				<td><input type='password' name='password'></td>
  			</tr>
  		</table>
  		<input type='submit' value='Submit'>
  	</form>
  </body>
</html>
