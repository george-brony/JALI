import Token
import re

tokenDatas = [
	[ "^((-)?[0-9]+)", Token.INT ],
	[ "^([a-zA-Z][a-zA-Z0-9]*)", Token.IDENTIFIER ],
	[ "^(\\+)", Token.PLUS ],
	[ "^(\\-)", Token.MINUS ]
]

# Разбивает строку на токены

class Tokenizer:
	def __init__(self, line):
		self.line = line
		self.currenToken = None

	def convert(self, type, value):
		if type == Token.INT:
			return int(value)
		elif type == Token.PLUS or type == Token.MINUS or Token.IDENTIFIER:
			return value

	def printError(self, error):
		raise Exception("Error parsing input: " + error)

	def getNextToken(self):
		self.line = self.line.strip()

		if not self.hasNextToken():
			return Token.Token(Token.EOF, None)

		for tokenData in tokenDatas:
			result = re.match(tokenData[0], self.line)

			if result:
				self.line = self.line.replace(result.group(1), "", 1)
				return Token.Token(tokenData[1], self.convert(tokenData[1], result.group(1)))

		self.printError("Token type is not defined")

	def hasNextToken(self):
		if len(self.line) > 0:
			return True
		else:
			return False