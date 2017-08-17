
def base3(base, msg):
	for m in msg.split(" "):
		x = 0
		print(m)
		for i in m:
			x *= base
			x += int(i)
		print(chr(x),x)