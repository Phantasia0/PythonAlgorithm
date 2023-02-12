import sys
import heapq

sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())

nums = list(map(int, input().split()))

res = [(nums[i], i) for i in range(n)]

heapq._heapify_max(res)
cnt = 0

while res:
    item = heapq._heappop_max(res)
    print(item)
    cnt += 1
    if item[1] == m:
        break

print(cnt)


# CANT FIT HEAP
