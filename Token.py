INT, PLUS, MINUS, MULTIPLY, DIVIDE, IDENTIFIER, EOF = "int", "+", "-", "*", "/", "identifier", "EOF"

class Token(object):
	def __init__(self, type, value):
		self.type = type
		self.value = value

	def __str__(self):
		return "Token: [{type} : {value}]".format(
			type = self.type,
			value = repr(self.value)
		)

	def __repr__(self):
		return self.__str__()

	def getType(self):
		return self.type

	def getValue(self):
		return self.value