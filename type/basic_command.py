import requests
import json
from . import command_interface

class basic_command(command_interface.command_interface):
	def __init__(self, API_KEY="", API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom", prompt):
		API_URL = API_URL
		headers = {"Authorization": f"Bearer {API_KEY}"}
		prompt = prompt

	def query(payload):
		response = requests.post(API_URL, headers=headers, json=payload)
		return response.json()

	def predict(self, input):
		return "test"