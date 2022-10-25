from bottle import request, Bottle, template, redirect, response
import subprocess
import io

from model import Problem, User, load_state, save_state, Submission

state = load_state("state.json")

with open('secret.txt') as f:
    secret = f.read()

def list_problems():
	if ((username := request.get_cookie("username", secret=secret)) 
			and not (user := find_user(username))):
		return template("error", error="Neveljaven piškotek.")
	return template("problem_list", problems=state.problems, username=username)

def show_problem(problem_id):
	if ((username := request.get_cookie("username", secret=secret)) 
			and not (user := find_user(username))):
		return template("error", error="Neveljaven piškotek.")
	return template("problem", problem=state.problems[problem_id], id=problem_id, username=username)
	
def submit(problem_id):
	if not (username := request.get_cookie("username", secret=secret)):
		return template("error", error="Nisi prijavljen")
	if not (user := find_user(username)):
		return template("error", error="Neveljaven piškotek.")
	problem = state.problems[problem_id]
	if f := request.files.get("file"):
		c = f.file.read()
		s = 0
		with open("sub.py", "wb") as sub:
			sub.write(c)
		tests=len(problem.input)
		results = []
		for test in range(0, tests):
			try:
				process = subprocess.run(["python3", "sub.py"],
					capture_output=True,
					input=problem.input[test].encode("utf-8"),
					timeout=problem.time_limit)
			except:
				results.append("TLE")
			else:
				if process.returncode != 0:
					results.append("RTE")
				elif process.stdout == problem.output[test].encode("utf-8"):
					results.append("OK")
					s += 1
				else:
					results.append("WA")
		sub = Submission(
			problem_id=problem_id,
			content=c.decode("utf-8"),
			results=results,
			score=s
		)
		user.submissions.append(sub)
		save_state("state.json", state)
		return template("submission", results=results, username=username, problem=problem)
	else:
		return template("error", error="Manjkajoče datoteke.", username=username)

def create_problem():
	if ((username := request.get_cookie("username", secret=secret)) 
			and not (user := find_user(username))):
		return template("error", error="Neveljaven piškotek.")
	return template("create_problem", username=username)

def submit_problem():
	if not (username := request.get_cookie("username", secret=secret)):
		return template("error", error="Nisi prijavljen")
	if not (user := find_user(username)):
		return template("error", error="Neveljaven piškotek.")
	t = request.forms.get("title")
	tl = request.forms.get("time_limit")
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
		time_limit=tl,
		input=inp,
		output=outp,
	)
	state.problems.append(problem)
	save_state("state.json", state)
	problem_id = len(state.problems)-1
	redirect("/" + str(problem_id))
		
def login_prompt():
	return template("login")
	
def check_password(p1,  p2):
	return p1 == p2
	
def find_user(username):
	for user in state.users:
		if username == user.username:
			return user		
	return None

def login():
	username = request.forms.get("username")
	password = request.forms.get("password")	
	if not (user := find_user(username)):
		return template("error", error="Uporabnika ni v bazi.")
	if not check_password(password, user.password):	
		return template("error", error="Uporabniško ime in geslo se ne ujemata.")
	response.set_cookie("username", username, path="/", secret=secret)
	redirect("/")			

def logout():
	response.delete_cookie('username', path='/', secret=secret)
	redirect("/")

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
		submissions=[]
	)
	state.users.append(user)
	save_state("state.json", state)
	state.username = un
	redirect("/login")

def number_of_submissions(problem_id, submissions):
	for sub in submissions:
		if sub.problem_id == problem_id:
			return True
	return False

def submissions(problem_id):
	if not (username := request.get_cookie("username", secret=secret)):
		return template("error", error="Nisi prijavljen")
	if not (user := find_user(username)):
		return template("error", error="Neveljaven piškotek.")
	problem = state.problems[problem_id]
	return template("submissions_list", submissions=user.submissions, problem=problem, id=problem_id, tried=(number_of_submissions(problem_id, user.submissions)), username=username)
	
def submission_details(problem_id, submission_number):
	if not (username := request.get_cookie("username", secret=secret)):
		return template("error", error="Nisi prijavljen")
	if not (user := find_user(username)):
		return template("error", error="Neveljaven piškotek.")
	problem = state.problems[problem_id]
	return template("submission_details", submission=user.submissions[submission_number], username=username, num=submission_number, problem=problem)

