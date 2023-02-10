import sys
import math

# sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

left = 0
right = len(nums) - 1

while left <= right:
    middle = math.floor(left + (right - left) / 2)

    if nums[middle] < m:
        left = middle + 1
    else:
        right = middle - 1

print(left + 1)
