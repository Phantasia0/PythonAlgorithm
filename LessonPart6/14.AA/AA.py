import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
maxX = -24700000
for i in range(n):
    for j in range(n):
        if maxX < area[i][j]:
            maxX = area[i][j]

dQ = deque()
twores = []

for i in range(maxX):
    cnt = 0
    check = [[0] * n for _ in range(n)]
    res = []
    for j in range(n):
        for k in range(n):
            if check[j][k] == 0:
                if area[j][k] > i:
                    dQ.append((j, k))
                    cnt = 1
                    check[j][k] = 1
                    while dQ:
                        temp = dQ.popleft()
                        for s in range(4):
                            x = temp[0] + dx[s]
                            y = temp[1] + dy[s]

                            if 0 <= x < n and 0 <= y < n:
                                if check[x][y] == 0:
                                    check[x][y] = 1
                                    if area[x][y] > i:
                                        dQ.append((x, y))
                                        cnt += 1
                    res.append(cnt)
    twores.append(res)

twores = list(map((lambda x: len(x)), twores))

print(max(twores))
