import sys

sys.stdin = open("input.txt", "rt")
from collections import deque


grid = [list(map(int, input().split())) for _ in range(7)]
ch = [[0] * 7 for _ in range(7)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

dQ = deque()

dQ.append((0, 0))
ch[0][0] = 1
min = 2222222222222
cnt = 0
isFinished = False

while dQ:
    if isFinished:
        break

    size = len(dQ)

    for i in range(size):
        now = dQ.popleft()
        if now[0] == 6 and now[1] == 6:
            if cnt < min:
                min = cnt
            isFinished = True
            break

        for j in range(4):
            x = now[0] + dx[j]
            y = now[1] + dy[j]
            if 0 <= x < 7 and 0 <= y < 7:
                if ch[x][y] == 0:
                    if grid[x][y] == 0:
                        dQ.append((x, y))
                        ch[x][y] = 1
    cnt += 1


if min == 2222222222222:
    print(-1)
else:
    print(min)
