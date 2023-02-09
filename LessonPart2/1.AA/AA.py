import sys
import math

#sys.stdin = open("input.txt")

n = int(input())

for i in range(n):
    str = input().lower()
    if len(str) % 2 == 0:
        cnt = math.floor(len(str) / 2 + 0.5)
        if str[0:cnt] == str[: cnt - 1 : -1]:
            print("{}{} YES".format("#", i + 1))
        else:
            print("{}{} NO".format("#", i + 1))
    else:
        cnt = math.floor(len(str) / 2 + 0.5)
        if str[0 : cnt - 1] == str[: cnt - 1 : -1]:
            print("{}{} YES".format("#", i + 1))
        else:
            print("{}{} NO".format("#", i + 1))
