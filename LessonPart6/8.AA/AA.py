import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

n = int(input())

grid = [[0] * n for _ in range(n)]
check = [[0] * n for _ in range(n)]

for i in range(n):
    grid[i] = list(map(int, input().split()))

dQ = deque()

dQ.append((n // 2, n // 2))
check[n // 2][n // 2] = 1

cnt = 0
sum = grid[n // 2][n // 2]
L = 0
while dQ:
    if L == n // 2:
        break
    size = len(dQ)

    for i in range(size):
        now = dQ.popleft()

        for next in (now[0] - 1, now[0] + 1):
            if check[next][now[1]] == 0:
                dQ.append((next, now[1]))
                sum += grid[next][now[1]]
                check[next][now[1]] = 1
        for next in (now[1] - 1, now[1] + 1):
            if check[now[0]][next] == 0:
                dQ.append((now[0], next))
                sum += grid[now[0]][next]
                check[now[0]][next] = 1

    L += 1

print(sum)
