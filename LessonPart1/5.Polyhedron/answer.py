import sys

sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
cnt = [0] * (n + m + 1)
maxNum = float("-inf")
for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt[i + j] += 1

maxNum = max(cnt)

for i in range(n + m + 1):
    if cnt[i] == maxNum:
        print(i, end=" ")
