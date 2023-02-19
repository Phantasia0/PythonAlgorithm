import sys
from collections import deque


def getDistance(arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                pizzaQ.append((i, j))
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                homeQ.append((i, j))
    minX = 2470000
    for i in homeQ:
        for j in pizzaQ:
            dist = abs(i[0] - j[0]) + abs(i[1] - j[1])
            if dist < minX:
                minX = dist
        distQ.append(minX)
        minX = 247000

    return sum(distQ)


def DFS(L, s, sums):
    distQ.clear()

    if L == m:
        minX = 2470000
        for i in homeQ:
            for j in res:
                dist = abs(i[0] - j[0]) + abs(i[1] - j[1])
                if dist < minX:
                    minX = dist
            distQ.append(minX)
        result = sum(distQ)
        
    else:
        for i in range(s, len(pizzaQ)):
            res.append(pizzaQ[i])
            DFS(L + 1, i + 1)


sys.stdin = open("input.txt", "rt")

pizzaQ = deque()
homeQ = deque()
distQ = deque()

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
res = [0] * m

cnt = 0
for i in range(n):
    for j in range(n):
        if map[i][j] == 2:
            cnt += 1


# DFS(0, 0)
# getDistance()
print(res)
