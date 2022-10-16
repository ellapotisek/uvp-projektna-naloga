<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#ffffff">
    <title>Oddaja</title>
    <link rel="stylesheet" href="/static/main.css">
  </head>
  <body>
	Naloga uspešno oddana.<br>
	% for i, res in enumerate(results):
		{{i+1}} {{res}}<br>
	% end
  </body>
</html>
