from bottle import request, Bottle, template, redirect
import subprocess
import io

from model import Problem, User, load_state, save_state

state = load_state("state.json")
state.username = None

def list_problems():
	return template("problem_list", problems=state.problems, username=state.username)

def show_problem(problem_id):
	return template("problem", problem=state.problems[problem_id], id=problem_id)
	
def submit(problem_id):
	if state.username == None:
		return template("error", error="Nisi prijavljen")
	problem = state.problems[problem_id]
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
	if state.username == None:
		return template("error", error="Nisi prijavljen")
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
	state.problems.append(problem)
	save_state("state.json", state)
	problem_id = len(state.problems)-1
	return redirect("/" + str(problem_id))
		
def login_prompt():
	return template("login")

def login():
	un = request.forms.get("username")
	p = request.forms.get("password")
	if state.username != None:
		return template("error", error="Nekdo je ze prijavljen")
	for user in state.users:
		if un == user.username:
			if p == user.password:
				state.username = un
				return redirect("/")
			else:
				return template("error", error="Uporabniško ime in geslo se ne ujemata.")
	return template("error", error="Uporabnika ni v bazi")

def logout():
	state.username = None
	return redirect("/")

def new_user_prompt():
	return template("new_user")

def new_user():
	un = request.forms.get("username")
	p = request.forms.get("password")
	cp = request.forms.get("confirm_password")
	if p != cp:
		return template("error", error="Gesli se ne ujemata")
	user = User(
		username=un,
		password=p,
		progress=[]
	)
	state.users.append(user)
	save_state("state.json", state)
	state.username = un
	return redirect("/")

