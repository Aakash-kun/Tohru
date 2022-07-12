from typing import Union
import json


class Config:
	def __init__(self, fn: str) -> None:
		self.fn: str = fn
		self.config: dict = json.load(open(fn))

	def update(self, key: Union[dict, str], value: Union[dict, str, int, list]) -> None:
		self.config[key] = value
		json.dump(self.config, open(self.fn, "w"), indent=4)

	def get(self, key: Union[str, dict]) -> Union[dict, str, int, list]:
		self.config: dict = json.load(open(self.fn))
		return self.config[key]
