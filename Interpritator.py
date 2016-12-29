import Token
from Tokenizer import Tokenizer

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

	def multiplyTwoTokens(self):
		first = self.stack[-2]
		second = self.stack[-1]

		if first.getType() != second.getType():
			self.printError("Couldn't multiply " + first.getType() + " by " + second.getType())

		self.stack.pop();
		self.stack.pop();

		self.loadToken(Token.Token(first.getType(), first.getValue() * second.getValue()))

	def divideTwoTokens(self):
		first = self.stack[-2]
		second = self.stack[-1]

		if first.getType() != second.getType():
			self.printError("Couldn't divide " + first.getType() + " by " + second.getType())

		self.stack.pop();
		self.stack.pop();

		if second.getValue() == 0: # Doesn't work. Some how this code is not exuted. Error is in File "./jalrti.py", line 12
			printError("Division by zero")

		print(second.getValue())


		self.loadToken(Token.Token(first.getType(), first.getValue() / second.getValue()))

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
			elif type == Token.MULTIPLY:
				self.currenToken = self.tokenizer.getNextToken()
				self.loadToken(self.currenToken)
				self.multiplyTwoTokens()
			elif type == Token.DIVIDE:
				self.currenToken = self.tokenizer.getNextToken()
				self.loadToken(self.currenToken)
				self.divideTwoTokens()
			else:
				self.printError("Invalid token: " + slf.currenToken.getType())

		print(self.stack[-1].getValue())
