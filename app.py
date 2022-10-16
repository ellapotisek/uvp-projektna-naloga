from bottle import request, Bottle, template, redirect
import subprocess
import io

from model import Problem, load_state, save_state

problems = load_state("state.json")

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
				results.append("RTE")
			elif process.stdout == problem.output[test].encode("utf-8"):
				results.append("OK")
			else:
				results.append("WA")
		return template("submission", results=results)
	else:
		raise Exception()

def create_problem():
	return template("create_problem")

def submit_problem():
	t = request.forms.get("title")
	if f := request.files.getall("content"):
		txt = f[0].file.read().decode("utf-8")
	inp = []
	if i := request.files.getall("input"):
		for p in i:
			inp.append(p.file.read().decode("utf-8"))
	outp = []
	if o := request.files.getall("output"):
		for p in o:
			outp.append(p.file.read().decode("utf-8"))
	problem = Problem(
		title=t,
		content=txt,
		input=inp,
		output=outp,
	)
	problems.append(problem)
	save_state("state.json", problems)
	problem_id = len(problems)-1
	return redirect("/" + str(problem_id))
		
	

app.route("/<problem_id:int>/upload", "POST", submit)
app.route("/", "GET", list_problems)
app.route("/<problem_id:int>", "GET", show_problem)
app.route("/create_problem", "GET", create_problem)
app.route("/create_problem/upload", "POST", submit_problem)

app.run(host='localhost', port=8080, debug=True, reload=True)
