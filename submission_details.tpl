<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#ffffff">
    <title>Podrobnosti oddaj</title>
    <link rel="stylesheet" href="/static/main.css">
  </head>
  <body>
	% for i, sub in enumerate(submission.results):
		{{i+1}} {{sub}}<br>
	% end
  </body>
</html>
