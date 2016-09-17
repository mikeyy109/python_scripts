import random

rtn = ["Yes definetly!", "I think so yes.", "Probaly..", "Hmm not sure", "Maybe", "Probaly not", "I dont think so", "Definetly not!"]
gLoop = True

def ball():
	x = random.randint(0,7)
	print(rtn[x])
	print("\n\n")

print("-------8 Ball-------")
print("--------------------")
print("\n\n")

while gLoop:
	print("Think of a question for the great 8 Ball..\n")
	a = input("press enter when ready... ('x' to quit)\n")
	if a == "x":
		gLoop = False
		break
	print("--------------------")
	ball()

print("####################")
print("#### Game Over #####")
print("####################")