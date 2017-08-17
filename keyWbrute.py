#!python3
import argparse
import hashlib
global count
count = 0

def test(string, curHash):
	global count
	y = hashlib.sha512()
	y.update(str.encode(string))
	if y.hexdigest() == curHash:
		count += 1
		print("I did it! %s" % string)
		return string
	else:
		count += 1
		return 0

def numBrute():
	complete_list = []
	for y in range(100):
		complete_list.append(str(y))
	for x in range(10):
		x = '0' + str(x)
		complete_list.append(x)
	return complete_list


def dictionary_attack(dict_file, cHash):
	x = 0
	f = open(dict_file, 'r')
	for y in f:
		a = test(y[0:len(y) - 1], cHash)
		if a != 0:
			return a
	return None

def method(num, avail, curHash, file):
	if num == 1:
		numbers = numBrute()
		for h1 in range(2):
			for x1 in range(2):
				for y1 in range(2):
					for c1 in range(len(avail)):
						for l1 in range(len(avail)):
							for e1 in range(len(avail)):
								if y1 == 0:
									if x1 == 0:
										if h1 == 0:
											a1 = test(avail[c1][e1].lower() + avail[l1], curHash)
											print(avail[c1][e1].lower() + avail[l1])
										else:
											for p in range(len(numbers)):
												test(avail[c1][e1].lower() + avail[l1] + numbers[p], curHash)
									else:
										if h1 == 0:
											a1 = test(avail[c1][e1].lower() + avail[l1][1:], curHash)
											print(avail[c1][e1].lower() + avail[l1][1:])
										else:
											for p in range(len(numbers)):
												a1 = test(avail[c1][e1].lower() + avail[l1][1:] + numbers[p], curHash)

								else:
									if x1 == 0:
										if h1 == 0:
											a1 = test(avail[c1][e1] + avail[l1].lower(), curHash)
											print(avail[c1][e1] + avail[l1].lower())
										else:
											for p in range(len(numbers)):
												a1 = test(avail[c1][e1] + avail[l1].lower() + numbers[p], curHash)
									else:
										if h1 == 0:
											a1 = test(avail[c1][e1] + avail[l1][1:].lower(), curHash)
											print(avail[c1][e1] + avail[l1][1:].lower())
										else:
											for p in range(len(numbers)):
												a1 = test(avail[c1][e1] + avail[l1][1:].lower() + numbers[p], curHash)
								if a1 != 0:
									return a1
	elif num == 2:
		dictionary_attack(file, curHash)
	
	return 0
#	elif num == 2:



def main(curHash, avail, dict_file):
	print(avail)
	global count
	for y in range(2):
		 a = method(y + 1, avail, curHash, dict_file)
		 if a != 0:
		 	return a
	print("Count = " + str(count))
			


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = "A bruteforce with keywords")
	parser.add_argument("Hash", action="store", type=str)

	parser.add_argument("-n", "--firstName", action="store", type=str)
	parser.add_argument("-l", "--lastName", action="store", type=str)
	parser.add_argument("-p", "--petName", action="store", type=str)
	parser.add_argument("-s", "--sport", action="store", type=str)
	parser.add_argument("-d", "--dict_file", action="store", default = "crackstation.txt", type=str)
	args = parser.parse_args()
	x = "".join(str(args.firstName) + " " + str(args.lastName) + " " + str(args.petName) + " " + str(args.sport))
	x = x.split(" ")
	z = []
	for y in range(len(x)):
		if x[y] != "None":
			z.append(x[y])
	main(args.Hash, z, args.dict_file)



