import sys
import math

sys.stdin = open("input.txt", "rt")


def Count(len):
    cnt = 1
    endPoint = coords[0]
    for i in range(1, n):
        if coords[i] - endPoint >= len:
            cnt += 1
            endPoint = coords[i]
    return cnt


n, c = map(int, input().split())

coords = []
for i in range(n):
    coords.append(int(input()))


coords.sort()
left = 1
right = coords[n - 1]

while left <= right:
    mid = (left + right) // 2
    if Count(mid) >= c:
        res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)
