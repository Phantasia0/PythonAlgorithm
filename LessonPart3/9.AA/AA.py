import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

n = int(input())
nums = list(map(int, input().split()))

nums = deque(nums)
res = [(0, 0)]

while True:
    if len(nums) == 0:
        break

    if len(nums) == 1:
        if nums[0] > res[len(res) - 1]:
            res.append((nums[0], 0))
            break
        else:
            break
    else:
        if nums[0] < nums[-1]:
            if res[len(res) - 1][0] < nums[0]:
                res.append((nums.popleft(), 0))
            else:
                res.append((nums.pop(), 1))
        else:
            if res[len(res) - 1][0] < nums[-1]:
                res.append((nums.pop(), 1))
            else:
                res.append((nums.popleft(), 0))

        if res[len(res) - 1][0] > nums[0] and res[len(res) - 1][0] > nums[-1]:
            break

res.pop(0)
print(len(res))
for value, idx in res:
    if idx == 0:
        print("L", end="")
    elif idx == 1:
        print("R", end="")
