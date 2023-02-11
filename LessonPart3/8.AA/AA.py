import sys

sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)

cnt = 0
while len(nums) > 0:
    bM = nums.pop(0)
    for j in range(len(nums)):
        if bM + nums[j] <= m:
            nums.pop(j)
            cnt += 1
            break
    else:
        cnt += 1

print(cnt)
