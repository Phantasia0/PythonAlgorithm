import sys

sys.stdin = open("input.txt", "rt")

n = int(input())
blocks = []
for i in range(n):
    width, height, weight = map(int, input().split())
    blocks.append((width, height, weight, i + 1))

blocks.sort(reverse=True)

dp = [[] for _ in range(n)]
dp[0] = [blocks[0]]
res = blocks[0][1]

for i in range(1, n):
    mh = 0
    max_h = []
    for j in range(i - 1, -1, -1):
        height = 0
        for value in dp[j]:
            height += value[1]
        if blocks[j][2] > blocks[i][2] and height > mh:
            mh = height
            max_h = dp[j][:]
    max_h.append(blocks[i])
    res = max(res, mh + blocks[i][1])
    dp[i] = max_h

for value in dp:
    sum = 0
    for x in value:
        sum += x[1]
    if sum == res:
        print(len(value))
        for y in reversed(value):
            print(y[3])
