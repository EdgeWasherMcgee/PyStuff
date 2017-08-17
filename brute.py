def bruteXorString(string):
	string = string.split(" ")
	for x in range(255):
		c = []
		for y in string:
			c.append(chr(x ^ int(y)))
		c = "".join(c)
		print(c)

