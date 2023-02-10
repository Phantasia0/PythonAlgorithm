import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
nums = list(map(int, input().split()))

head = 0
tail = 0
cnt = 0
sum = 1

while head < len(nums) and tail < len(nums):
    if sum < m:
        tail += 1
        if tail == len(nums):
            break
        sum += nums[tail]
    elif sum == m:
        print(head, tail)
        cnt += 1
        if head < tail:
            sum -= nums[head]
            head += 1
        else:
            tail += 1
            sum += nums[tail]
    elif sum > m:
        sum -= nums[head]
        head += 1

print(cnt)
