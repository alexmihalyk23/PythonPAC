import argparse
from math import factorial

parser = argparse.ArgumentParser(
                    prog='Lab2',
                    description='Pascal Triangle',
                    epilog='Pascal Triangle prog')
parser.add_argument('-n', '--num',type=int)


args = parser.parse_args()

def pascal_triangle(n):
    for i in range(n):
        for j in range(n-i+1):
            print(end = " ")
        for j in range(i+1):
            print(factorial(i)//(factorial(i-j) * factorial(j)), end=" ")
        print()


pascal_triangle(args.num)


