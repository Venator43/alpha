import requests
import json
from . import command_interface

class basic_command(command_interface.command_interface):
	def __init__(self, API_KEY, API_URL, prompt):
		self.API_URL = API_URL
		self.headers = {"Authorization": f"Bearer {API_KEY}"}
		self.prompt = 'Mohon nyalakan lampu atas\n>{"device_type" : "lamp", "command" : "on", "device_identifier" : "atas"}[EOS]\nMatikan lampu kamar depan\n>{"device_type" : "lamp", "command" : "off", "device_identifier" : "kamar depan"}[EOS]\nMatikan lampu depan\n>{"device_type" : "lamp", "command" : "off", "device_identifier" : "depan"}[EOS]\nTolong nyalakan komputer di dapur\n>{"device_type" : "PC", "command" : "on", "device_identifier" : "dapur"}[EOS]\nNyalakan TV di tempat tidur\n>{"device_type" : "TV", "command" : "on", "device_identifier" : "Tempat Tidur"}[EOS]\nMatikan microwave dapur\n>{"device_type" : "microwave", "command" : "off", "device_identifier" : "dapur"}[EOS]\ntolong nyalakan device nomer satu\n>{"device_type" : "device", "command" : "on", "device_identifier" : "satu"}[EOS]\nnyalakan oven di ruang tamu\n>\n'

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