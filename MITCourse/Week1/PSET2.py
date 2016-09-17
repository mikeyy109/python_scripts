testString = "oboonobobbobrbyobooobbobbtfoioboooobobo" # 4

word = "bob"
count = 0


for i in range(len(testString)):
	if testString[i:i+3] == word:
		count += 1
		
print("Number of times bob occurs is: " + str(count))


