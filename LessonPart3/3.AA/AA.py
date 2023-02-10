import sys

sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
songs = list(map(int, input().split()))


def count(k, idx, cnt):
    if idx == len(songs):
        return cnt

    sum = 0
    for i in range(idx, len(songs)):
        sum += songs[i]
        if sum > k:
            cnt += 1
            idx = i
            break
    else:
        idx = len(songs)
    cnt = count(k, idx, cnt)
    return cnt


left = max(songs)
right = 10000000

while left <= right:
    mid = int(left + (right - left) / 2)

    if count(mid, 0, 1) > m:
        left = mid + 1
    else:
        right = mid - 1

print(left)
