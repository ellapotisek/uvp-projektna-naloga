from dataclasses import dataclass
from typing import List
import json

@dataclass
class Submission:
	problem_id: int
	content: str
	results: List[str]
	score: int
	
	def to_dict(self):
		return {
			"problem_id": self.problem_id,
			"content": self.content,
			"results": self.results,
			"score": self.score
		}
	
	@classmethod
	def from_dict(cls, d):
		return cls(
			problem_id=d["problem_id"],
			content=d["content"],
			results=d["results"],
			score=d["score"]
		)
		

@dataclass
class Problem:
	title: str
	content: str
	time_limit: int
	input: List[str]
	output: List[str]
	
	def to_dict(self):
		return {
			"title": self.title,
			"content": self.content,
			"time_limit": self.time_limit,
			"input": self.input,
			"output": self.output
		}
		
	@classmethod
	def from_dict(cls, d):
		return cls(
			title=d["title"],
			content=d["content"],
			time_limit=d["time_limit"],
			input=d["input"],
			output=d["output"]
		)

@dataclass
class User:
	username: str
	password: str
	submissions: List[Submission]
	
	def to_dict(self):
		return {
			"username": self.username,
			"password": self.password,
			"submissions": list(map(lambda i: i.to_dict(), self.submissions))
		}
		
	@classmethod
	def from_dict(cls, d):
		return cls(
			username=d["username"],
			password=d["password"],
			submissions=list(map(Submission.from_dict, d["submissions"]))
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
