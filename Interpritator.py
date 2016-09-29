import Token
from Tokenizer import Tokenizer

# Копается в токенах и парсит их

class Interpritator:
	def __init__(self, tokenizer):
		self.tokenizer = tokenizer;
		self.stack = []

	def loadToken(self, token):
		self.stack.append(token)

	def addTwoTokens(self):
		first = self.stack[-2]
		second = self.stack[-1]

		if first.getType() != second.getType():
			self.printError("Couldn't add " + first.getType() + " to " + second.getType())

		self.stack.pop();
		self.stack.pop();

		self.loadToken(Token.Token(first.getType(), first.getValue() + second.getValue()))

	def subtractTwoTokens(self):
		first = self.stack[-2]
		second = self.stack[-1]

		if first.getType() != second.getType():
			self.printError("Couldn't subtract " + first.getType() + " from " + second.getType())

		self.stack.pop();
		self.stack.pop();

		self.loadToken(Token.Token(first.getType(), first.getValue() - second.getValue()))

	def printError(self, error):
		raise Exception("Error parsing token tree: " + error)

	def parse(self):
		while self.tokenizer.hasNextToken():
			self.currenToken = self.tokenizer.getNextToken()
			type = self.currenToken.getType()

			if type == Token.INT:
				self.loadToken(self.currenToken)
			elif type == Token.PLUS:
				self.currenToken = self.tokenizer.getNextToken()
				self.loadToken(self.currenToken)
				self.addTwoTokens()
			elif type == Token.MINUS:
				self.currenToken = self.tokenizer.getNextToken()
				self.loadToken(self.currenToken)
				self.subtractTwoTokens()
			else:
				self.printError("Invalid token: " + slf.currenToken.getType())

		print(self.stack[-1].getValue())
