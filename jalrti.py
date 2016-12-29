from Token import Token
from Tokenizer import Tokenizer
from Interpritator import Interpritator

debug = True

if debug:
	print("Debug mode is on")

while(True):
	try:
		code = input(">>> ")
	except EOFError:
		break

	if not code:
		continue

	interpritator = Interpritator(Tokenizer(code))
	interpritator.parse()