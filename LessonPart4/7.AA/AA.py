import sys
from collections import deque

# sys.stdin = open("input.txt", "rt")

order = input()
n = int(input())

order = list(order[i] for i in range(len(order)))
origin = order[:]

origin = deque(origin)
order = deque(order)

isBreaked = False
for i in range(n):
    s = input()
    for char in s:
        if isBreaked:
            break
        if order:
            if char == order[0]:
                order.popleft()
            else:
                for k in range(1, len(order)):
                    if char == order[k]:
                        isBreaked = True
                        break

    if len(order) > 0:
        print("{}{} NO".format("#", i + 1))
    else:
        print("{}{} YES".format("#", i + 1))

    order.clear()
    for i in range(len(origin)):
        order.append(origin[i])
    isBreaked = False
