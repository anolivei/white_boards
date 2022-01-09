import itertools

def decompondo():
	max_num = int(input().rstrip("\n"))
	ret = 0
	for i in itertools.product(range(0, max_num + 1), repeat=4):
		if (sum(i)) == 21:
			ret += 1
			# print(i)
			print(str(i[0]) + str(i[1]) + str(i[2]) + str(i[3]))
	if ret == 0:
		print('null')

if __name__ == '__main__':
	decompondo()

