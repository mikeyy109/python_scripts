# Finding UK mobile numbers in any text input

def isUKNum(text):
	if len(text) != 11:
		return False
	if text[0:1] != "07":
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

message = "This is a text message, first number 07837492044, 0172319382, 283881, 07281, 07372849533, 555-222-5555, 22-333-4444-222, 000-222-1111 test case over."

for i in range(len(message)):
	chunkUK = message[i:i+11]
	chunkUS = message[i:i+12]
	if isUKNum(chunkUK):
		print("UK Number found: " + chunkUK)
	if isUSNum(chunkUS):
		print("US Number found: " + chunkUS)
print("Done")

