import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

n = int(input())
grid = [list(map(int, input())) for _ in range(n)]

ch = [[0] * n for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
dQ = deque()
res = []


def FindMap(start, end):
    homeCount = 0
    dQ.append((start, end))

    while dQ:
        size = len(dQ)

        for i in range(size):
            tmp = dQ.popleft()
            if ch[tmp[0]][tmp[1]] == 0:
                ch[tmp[0]][tmp[1]] = 1
                if grid[tmp[0]][tmp[1]] == 1:
                    grid[tmp[0]][tmp[1]] = 0
                    homeCount += 1
            for j in range(4):
                x = tmp[0] + dx[j]
                y = tmp[1] + dy[j]

                if 0 <= x < n and 0 <= y < n:
                    if ch[x][y] == 0:
                        ch[x][y] = 1
                        if grid[x][y] == 1:
                            dQ.append((x, y))
                            grid[x][y] = 0
                            homeCount += 1
    res.append(homeCount)


for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            FindMap(i, j)

res.sort()

print(len(res))
for value in res:
    print(value)
