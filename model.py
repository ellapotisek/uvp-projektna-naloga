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
		
def load_state(fname):
	with open(fname) as f:
		p = json.load(f)
	return list(map(Problem.from_dict, p))
	
def save_state(fname, problems):
	p = list(map(lambda i: i.to_dict(), problems))
	with open(fname, "w") as f:
		json.dump(p, f)
