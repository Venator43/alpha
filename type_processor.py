import argparse
import sys
import pydoc

import yaml
from addict import Dict as Adict

class type_processor:
	def __init__(self, config_path):
		self.config_path = config_path
		self.type_dict = {}
		
		with open(config_path) as configfile:
			config = Adict(yaml.load(configfile, Loader=yaml.SafeLoader))
		
		analyzer_list = [t for t in config.type_list]
		for i in analyzer_list:
			type_name = i["type_name"]
			type_object = i["type_object"]
			type_parameter = i["type_param"]
			cur_analyzer = pydoc.locate(type_object)(**type_parameter)
			self.type_dict[type_name] = cur_analyzer

	def run(self, command_type, command_input, **kwargs):
		return self.type_dict[command_type].predict(command_input, **kwargs)
