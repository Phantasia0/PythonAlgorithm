import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())

MAX = 10000

check = [0] * (MAX + 1)
dis = [0] * (MAX + 1)

dis[n] = 0
check[n] = 1

dQ = deque()
dQ.append(n)

while dQ:
    now = dQ.popleft()

    if now == m:
        break

    for next in (now - 1, now + 1, now + 5):
        if 0 < next <= MAX:
            if check[next] == 0:
                dQ.append(next)
                check[next] = 1
                dis[next] = dis[now] + 1

print(dis[m])
