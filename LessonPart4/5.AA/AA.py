import sys
from collections import deque

# sys.stdin = open("input.txt", "rt")s

n, k = map(int, input().split())

queue = [i + 1 for i in range(n)]
queue = deque(queue)

cnt = 0
while len(queue) > 1:
    temp = queue.popleft()
    cnt += 1
    if cnt != k:
        queue.append(temp)
    else:
        cnt = 0

print(queue[0])
