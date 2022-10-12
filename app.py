from bottle import request, Bottle, template
import subprocess
import json

from model import Problem

with open("state.json") as f:
	p = json.load(f)
	
problems = []
for i in p:
	problems.append(Problem.from_dict(i))	

app = Bottle()

def list_problems():
	return template("problem_list", problems=problems)

def show_problem(problem_id):
	return template("problem", problem=problems[problem_id], id=problem_id)
	
def submit(problem_id):
	problem = problems[problem_id]
	if f := request.files.get("file"):
		with open("sub.py", "wb") as sub:
			sub.write(f.file.read())
		process = subprocess.run(["python3", "sub.py"], capture_output=True)
		if process.returncode != 0:
			return template("error", error="RTE")
		if process.stdout == problem.output.encode("utf-8"):
			res = "Odgovor je pravilen"
		else:
			res = "Odgovor ni pravilen"
		return template("submission", result=res)
	else:
		raise Exception()
	

app.route("/<problem_id:int>/upload", "POST", submit)
app.route("/", "GET", list_problems)
app.route("/<problem_id:int>", "GET", show_problem)

app.run(host='localhost', port=8000, debug=True, reload=True)
