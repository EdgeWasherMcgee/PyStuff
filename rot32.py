import base64

def rot(string, times):
	s = ''
	for y in string[:len(string) - 3]:
		s += chr((ord(y) - times) % 256)
	return s + string[len(string) - 3:]

def rot32(string):
	a = string
	for y in range(127):
		try:
			a = rot(string, y)
			b = base64.b32decode(a)
			print(b)
		except:
			print("%s didn't work" % a)
