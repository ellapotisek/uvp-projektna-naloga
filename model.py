from dataclasses import dataclass
from typing import List
import json

@dataclass
class Problem:
	title: str
	content: str
	input: List[str]
	output: List[str]
	
	def to_dict(self):
		return {
			"title": self.title,
			"content": self.content,
			"input": self.input,
			"output": self.output
		}
		
	@classmethod
	def from_dict(cls, d):
		return cls(
			title=d["title"],
			content=d["content"],
			input=d["input"],
			output=d["output"]
		)

@dataclass
class User:
	username: str
	password: str
	progress: List[int]
	
	def to_dict(self):
		return {
			"username": self.username,
			"password": self.password,
			"progress": self.progress
		}
		
	@classmethod
	def from_dict(cls, d):
		return cls(
			username=d["username"],
			password=d["password"],
			progress=d["progress"]
		)

@dataclass
class State:
	users: List[User]
	problems: List[Problem]
	
	def to_dict(self):
		return {
			"users": list(map(lambda i: i.to_dict(), self.users)),
			"problems": list(map(lambda i: i.to_dict(), self.problems))
		}
	
	@classmethod
	def from_dict(cls, d):
		return cls(
			users=list(map(User.from_dict, d["users"])),
			problems=list(map(Problem.from_dict, d["problems"]))
		)		
		
def load_state(fname):
	with open(fname) as f:
		p = json.load(f)
	return State.from_dict(p)
	
def save_state(fname, state: State):
	p = state.to_dict()
	with open(fname, "w") as f:
		json.dump(p, f)
