import sys

sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
nums = list(map(int, input().split()))

lt = 0
rt = 1
tot = nums[0]
cnt = 0
while True:
    if tot < m:
        if rt < n:
            tot += nums[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= nums[lt]
        lt += 1
    else:
        tot -= nums[lt]
        lt += 1

print(cnt)
