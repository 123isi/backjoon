import math
import sys

input = sys.stdin.read
data = input().split()

a1 = int(data[0])
b1 = int(data[1])
a2 = int(data[2])
b2 = int(data[3])

common_denominator = b1 * b2

numerator = a1 * b2 + a2 * b1

gcd = math.gcd(numerator, common_denominator)

numerator //= gcd
common_denominator //= gcd

print(numerator, common_denominator)