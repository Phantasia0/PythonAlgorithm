import sys

sys.stdin = open("input.txt", "rt")

n = int(input())

coins = list(map(int, input().split()))

m = int(input())

coins.sort()

dp = [247000] * (m + 1)
dp[0] = 0

for i in range(n):
    for j in range(coins[i], m + 1):
        dp[j] = min(dp[j - coins[i]] + 1, dp[j])

print(dp[m])
