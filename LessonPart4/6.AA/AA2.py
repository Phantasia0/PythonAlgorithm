import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())

nums = list(map(int, input().split()))
res = [(nums[i], i) for i in range(n)]

nums.sort(reverse=True)
res = deque(res)
cnt = 0

while res:
    item = res.popleft()
    if item[0] != nums[cnt]:
        res.append(item)
    else:
        cnt += 1
        if item[1] == m:
            print(cnt)
            break
