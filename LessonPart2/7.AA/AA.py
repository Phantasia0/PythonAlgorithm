import sys

# sys.stdin = open("input.txt", "rt")

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

res = []
cnt = 0
for i in range(n):
    if i < (n - 1) / 2:
        res.append(nums[i][int((n - 1) / 2) - cnt : int((n - 1) / 2) + 1 + cnt])
        cnt += 1
    elif i == (n - 1) / 2:
        res.append(nums[i][:])
    else:
        cnt -= 1
        res.append(nums[i][int((n - 1) / 2) - cnt : int((n - 1) / 2) + 1 + cnt])

sumRes = 0
for x in res:
    sumRes += sum(x)

print(sumRes)
