import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
res = []
dx = [0, -1, 0, 1, 1, -1, -1, 1]
dy = [-1, 0, 1, 0, 1, -1, 1, -1]
cnt = 0

dQ = deque()
for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            map[i][j] = 0
            cnt = 1
            dQ.append((i, j))
            while dQ:
                temp = dQ.popleft()
                for k in range(8):
                    x = temp[0] + dx[k]
                    y = temp[1] + dy[k]

                    if 0 <= x < n and 0 <= y < n:
                        if map[x][y] == 1:
                            map[x][y] = 0
                            dQ.append((x, y))
                            cnt += 1
            res.append(cnt)

print(len(res))
