import sys

# sys.stdin = open("input.txt", "rt")


def DFS(L, sums):
    global s
    if L == k:
        if s >= sums > 0:
            res.add(sums)
    else:
        DFS(L + 1, sums + weights[L])
        DFS(L + 1, sums)
        DFS(L + 1, sums - weights[L])


k = int(input())
weights = list(map(int, input().split()))
weights.sort(reverse=True)

s = sum(weights)
res = set()
DFS(0, 0)

cnt = 0
for value in range(1, s):
    if value not in res:
        cnt += 1

print(cnt)
