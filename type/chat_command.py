import requests
import json
from . import command_interface

class chat_command(command_interface.command_interface):
	def __init__(self, API_KEY, API_URL, prompt = ''):
		self.API_URL = API_URL
		self.headers = {"Authorization": f"Bearer {API_KEY}"}
		self.prompt = prompt

	def query(self, payload):
		response = requests.post(self.API_URL, headers=self.headers, json=payload)
		return response.json()

	def predict(self, input_command):
		output = self.query({
		    "inputs": input_command,
		    "parameters": {"do_sample" : False, "return_full_text" : False}
		})
		output_dict = output[0]["generated_text"]
		# print(output_dict)
		return output_dict