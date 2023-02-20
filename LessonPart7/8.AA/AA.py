# 냅색 알고리즘
import sys

sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())


dp = [0] * (m + 1)

for i in range(n):
    w, v = map(int, input().split())
    for j in range(w, m + 1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[m])
