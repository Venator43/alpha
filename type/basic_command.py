import requests
import json
from . import command_interface

class basic_command(command_interface.command_interface):
	def __init__(self, API_KEY, API_URL, prompt = ''):
		self.API_URL = API_URL
		self.headers = {"Authorization": f"Bearer {API_KEY}"}
		self.prompt = prompt

	def query(self, payload):
		response = requests.post(self.API_URL, headers=self.headers, json=payload)
		return response.json()

	def predict(self, input_command):
		model_input = self.prompt + input_command + "\n>"
		output = self.query({
		    "inputs": model_input,
		    "parameters": {"do_sample" : False, "return_full_text" : False, "max_new_tokens" : 54}
		})
		output_dict = json.loads(output[0]["generated_text"].split("[EOS]")[0])
		# print(output_dict)
		return output_dict