import sys

sys.stdin = open("input.txt", "rt")

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
rots = [list(map(int, input().split())) for _ in range(m)]

for i in rots:
    rot = i
    if rot[1] == 0:
        for j in range(rot[2]):
            temp = nums[rot[0] - 1].pop(0)
            nums[rot[0] - 1].append(temp)
    else:
        for j in range(rot[2]):
            temp = nums[rot[0] - 1].pop()
            nums[rot[0] - 1].insert(0, temp)

s = 0
e = n - 1
res = 0
for i in range(n):
    for j in range(s, e + 1):
        res += nums[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)
