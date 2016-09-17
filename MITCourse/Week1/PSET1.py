testString = "eeeeeeeee" #answer is 6

vowls = "aeiou"
count = 0
currentS = ""
currentV = ""

for i in testString:
	currentS = i
	for v in vowls:
		currentV = v
		if currentS == currentV:
			count += 1

print("Number of vowls = " + str(count))

