from dataclasses import dataclass


@dataclass
class Problem:
	title: str
	content: str
	input: str
	output: str
	
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
