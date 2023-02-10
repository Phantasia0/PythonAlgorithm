import sys
import math

sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
nums = []
for i in range(n):
    nums.append(int(input()))

left = 1
right = max(nums)
res = []

while left <= right:
    mid = math.floor(left + (right - left) / 2)
    sum = 0

    for num in nums:
        sum += math.floor(num / mid)

    if sum >= k:
        left = mid + 1
    elif sum < k:
        right = mid - 1

print(left - 1)
