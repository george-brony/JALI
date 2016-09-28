#importing
import re

#debug mode
debug = True
if debug == True:
	print("Debug mode is on")
else:
	print("Debug mode is off")

#global initialization
global_varibles = {}
functions = {}

#functions definding
def main():


def functions_parser(code):
	#initialization

	#code
	if not "func " in code :
		return -1
	start_index = code.find("func ")
	if bracket_index = code.find("(") == -1:
		return -1
	name = code[start_index + 5 : bracket_index - 1]

def varibles_parser(code):
	#initialization



#run the programm
if __name__ == "__main__":
    main()
