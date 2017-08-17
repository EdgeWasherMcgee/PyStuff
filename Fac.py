#!python3
def Main(number):
		a = 1
		for i in range(number):
			a *= number - i
		return a

def fac(n):
	if n == 1:
		return 1
	return fac(n-1)*n

if __name__ == "__main__":
	inp = input("Of what do you want to have the fac of\n")
	answ = fac(int(inp))
	print("The %sth fac is %d" % (inp, answ))