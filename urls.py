import bottle
from app import *

app = bottle.Bottle()

def static():
	return bottle.static_file("main.css", "./")

app.route("/main.css", "GET", static)


app.route("/<problem_id:int>/upload", "POST", submit)
app.route("/", "GET", list_problems)
app.route("/<problem_id:int>", "GET", show_problem)
app.route("/create_problem", "GET", create_problem)
app.route("/create_problem/upload", "POST", submit_problem)
app.route("/login", "GET", login_prompt)
app.route("/login", "POST", login)
app.route("/logout", "GET", logout)
app.route("/new_user", "GET", new_user_prompt)
app.route("/new_user", "POST", new_user)
app.route("/<problem_id:int>/submissions", "GET", submissions)
app.route("/<problem_id:int>/submissions/<submission_number:int>", "GET", submission_details)

#app.run(host='localhost', port=8000, debug=True, reload=True)
