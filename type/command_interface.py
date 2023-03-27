class command_interface:
	def __init__(self):
		raise NotImplementedError()

	def predict(self, input):
		raise NotImplementedError()