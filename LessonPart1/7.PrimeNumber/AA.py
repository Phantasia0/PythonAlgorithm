import sys
import math

# sys.stdin = open("input.txt", "r")

n = int(input())

isPrime = [True] * (n + 1)
isPrime[0] = False
isPrime[1] = False

num = math.floor(math.sqrt(n))

for i in range(2, num + 1):
    if isPrime[i]:
        for j in range(i * 2, n + 1, i):
            isPrime[j] = False

result = list(filter(lambda x: x != False, isPrime))
print(len(result))
