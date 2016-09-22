import re

# Finding UK/US numbers in any text input

def isUKNum(text):
	if len(text) != 11:
		return False
	if text[0:2] != "07":
		return False
	for i in range(len(text)):
		if not text[i].isdecimal():
			return False
	return True

def isUSNum(text):
	if len(text) != 12:
		return False
	for i in range(0,3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4,7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8,12):
		if not text[i].isdecimal():
			return False
	return True

message = "-- This is a text message, first number 07837492044," \
		" 0172319382, 283881, 07281, 07372849533, 555-222-5555," \
		" 22-333-4444-222, 000-222-1111. +447291039488 224.567.3233 " \
		"922-203-4444 ex 32 07283940459 ---- END ----"

for i in range(len(message)):
	chunkUK = message[i:i+11]
	chunkUS = message[i:i+12]
	if isUKNum(chunkUK):
		print("UK Number found: " + chunkUK)
	if isUSNum(chunkUS):
		print("US Number found: " + chunkUS)
print("Done")

# Regular Expressions

rxUS = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
dataUS = rxUS.search(message)
print(dataUS.group(0))

rxUK = re.compile(r'07(\d){9}')
dataUK = rxUK.search(message)
print(dataUK.group(0))

