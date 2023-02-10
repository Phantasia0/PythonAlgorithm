import sys

# sys.stdin = open("input.txt", "rt")

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

grid = [[0] * (n + 2) for _ in range(n + 2)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        grid[i][j] = nums[i - 1][j - 1]

res = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        temp = grid[i][j]
        if (
            temp > grid[i - 1][j]
            and temp > grid[i + 1][j]
            and temp > grid[i][j - 1]
            and temp > grid[i][j + 1]
        ):
            res.append(temp)

print(len(res))
