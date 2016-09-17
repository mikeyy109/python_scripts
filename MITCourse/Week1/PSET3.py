testString = "stringherhehrhehhehr"

subString, subString2 = "", ""

for letter in testString:

	if subString == "":
		subString = letter
	elif letter >= subString[-1]:
		subString += letter
	elif letter < subString[-1]:
		if len(subString2) < len(subString):
			subString2 = subString
			subString = letter
		else:
			subString = letter

if (len(subString) > len(subString2)):
	print(subString)
else:
	print(subString2)







