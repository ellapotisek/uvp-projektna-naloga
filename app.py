from bottle import request, Bottle, template
import subprocess

app = Bottle()

def show_problem():
	return template("problem")
	
def submit():
	if f := request.files.get("file"):
		with open("sub.py", "wb") as sub:
			sub.write(f.file.read())
		process = subprocess.run(["python3", "sub.py"], capture_output=True)
		if process.returncode != 0:
			return template("error", error="RTE")
		if process.stdout == b"500\n":
			res = "Odgovor je pravilen"
		else:
			res = "Odgovor ni pravilen"
		return template("submission", result=res)
	else:
		raise Exception()
	

app.route("/", "GET", show_problem)
app.route("/upload", "POST", submit)

app.run(host='localhost', port=8000, debug=True, reload=True)
