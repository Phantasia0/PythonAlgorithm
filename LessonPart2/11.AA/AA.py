import sys

sys.stdin = open("input.txt", "rt")

nums = [list(map(int, input().split())) for _ in range(7)]

cntRow = 0
cntCol = 0
dx = [1, 2]
dy = [-1, -2]
for i in range(7):
    for j in range(2, 5):
        if all(nums[i][j + dx[k]] == nums[i][j + dy[k]] for k in range(2)):
            cntRow += 1
        if all(nums[j + dx[k]][i] == nums[j + dy[k]][i] for k in range(2)):
            cntCol += 1


print(cntCol + cntRow)
