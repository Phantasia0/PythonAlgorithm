import sys

sys.stdin = open("input.txt", "rt")


def DFS(x, y):
    if dp[x][y] > 0:
        return dp[x][y]
    if x == 0 and y == 0:
        return board[0][0]
    else:
        if y == 0:
            dp[x][y] = DFS(x - 1, y) + board[x][y]
        elif x == 0:
            dp[x][y] = DFS(x, y - 1) + board[x][y]
        else:
            dp[x][y] = min(DFS(x - 1, y), DFS(x, y - 1)) + board[x][y]
        return dp[x][y]


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]  # 메모이제이션용
print(DFS(n - 1, n - 1))
