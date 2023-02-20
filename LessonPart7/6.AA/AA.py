import sys

sys.stdin = open("input.txt", "rt")

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


dp = [[0] * n for _ in range(n)]

dp[0][0] = board[0][0]
for i in range(1, n):
    dp[0][i] = board[0][i] + dp[0][i - 1]
    dp[i][0] = board[i][0] + dp[i - 1][0]

for i in range(1, n):
    for j in range(1, n):
        if dp[i][j - 1] < dp[i - 1][j]:
            dp[i][j] = dp[i][j - 1] + board[i][j]
        else:
            dp[i][j] = dp[i - 1][j] + board[i][j]

print(dp[n - 1][n - 1])
