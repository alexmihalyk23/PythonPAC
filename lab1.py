import argparse
import random


parser = argparse.ArgumentParser(
                    prog='Lab1',
                    description='bubbleSort',
                    epilog='bubbleSort program')
parser.add_argument('-n', '--num',type=int)


args = parser.parse_args()
# print(args.num)
arr = []



for i in range(args.num):
	rnd = random.random()
	print(rnd)
	arr.append(rnd)

print()

for i in range(args.num):
	print(arr[i])


def bubble_sort(arr, n):
	for i in range(n):
		isSwaped = False

		for j in range(n-i-1):
			if(arr[j] > arr[j+1]):
				arr[j], arr[j+1] = arr[j+1], arr[j]
				isSwaped = True
		if(isSwaped == False):
			break


bubble_sort(arr, args.num)
print()
print(arr)


