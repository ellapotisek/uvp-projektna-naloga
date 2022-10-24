<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#ffffff">
    <title>Oddaje</title>
    <link rel="stylesheet" href="/static/main.css">
  </head>
  <body>
  	% if tried == False:
  		Te naloge še nisi oddal.
  	% else:
	%	 for i, sub in enumerate(submissions):
	%		if sub.problem_id == id:
				<a href="/{{id}}/submissions/{{i}}">{{i+1}}</a>
				{{problem.title}} {{sub.score}}/{{len(problem.input)}}<br>
	% end
  </body>
</html>
