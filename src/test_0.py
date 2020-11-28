from util import iohandler

inputFile = iohandler.begin(__file__)

# --- solution ---

# framework test - using last years IO manager this year too, it's not a beauty, but it works alright
inputStr = inputFile.readline()

# --- solution ---

iohandler.end(str(inputStr))
