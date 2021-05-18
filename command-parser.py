class Command():
	def __init__(self, command):
		self.program, self.arguments = self.tokenize(command)

	def tokenize(self, command):
		split = command.split()
		return split[0], split[1:]

	def output(self):
		print(self.program)
		print(self.arguments)

example = Command('sherlock --timeout 1 evan.iso')
example.output()
