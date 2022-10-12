from bottle import request, Bottle, template
import subprocess
import json
import io

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
		tests=len(problem.input)
		results=[]
		for test in range(0, tests):
			process = subprocess.run(["python3", "sub.py"],
				capture_output=True, input=problem.input[test].encode("utf-8"))
			if process.returncode != 0:
				#return template("error", error="RTE")
				results.append("RTE")
			elif process.stdout == problem.output[test].encode("utf-8"):
				#res = "Odgovor je pravilen"
				results.append("OK")
			else:
				#res = "Odgovor ni pravilen"
				results.append("WA")
		return template("submission", results=results)
	else:
		raise Exception()
	

app.route("/<problem_id:int>/upload", "POST", submit)
app.route("/", "GET", list_problems)
app.route("/<problem_id:int>", "GET", show_problem)

app.run(host='localhost', port=8000, debug=True, reload=True)
