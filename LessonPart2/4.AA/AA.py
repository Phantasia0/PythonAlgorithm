import sys

# sys.stdin = open("input.txt", "rt")

n = int(input())
numsN = list(map(int, input().split()))
m = int(input())
numsM = list(map(int, input().split()))

numsN.extend(numsM)
numsN.sort()
for num in numsN:
    print(num, end=" ")
