import sys

sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())

dp = [0] * (m + 1)

check = [0] * (n + 1)

for i in range(n):
    s, t = map(int, input().split())
    for j in range(t, m + 1):
        dp[j] = max(dp[j], dp[j - t] + s)


print(dp)
