import sys

# sys.stdin = open("input.txt", "rt")


def DFS(x, y):
    global cnt
    if x == end[0] and y == end[1]:
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx <= n - 1 and 0 <= yy <= n - 1:
                if grid[x][y] < grid[xx][yy]:
                    if ch[xx][yy] == 0:
                        ch[xx][yy] = 1
                        DFS(xx, yy)
                        ch[xx][yy] = 0


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * n for _ in range(n)]

minN = 24700000
maxN = -24700000
cnt = 0
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(n):
    for j in range(n):
        if grid[i][j] < minN:
            minN = grid[i][j]
            start = (i, j)

        if grid[i][j] > maxN:
            maxN = grid[i][j]
            end = (i, j)


ch[start[0]][start[1]] = 1
DFS(start[0], start[1])

print(cnt)
