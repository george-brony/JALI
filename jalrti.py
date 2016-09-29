from Token import Token
from Tokenizer import Tokenizer

debug = True
code = "+2"

if debug:
	print("Debug mode is on")

tokenizer = Tokenizer(code)

while tokenizer.hasNextToken():
	token = tokenizer.nextToken()
	print(token)