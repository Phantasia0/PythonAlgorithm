import sys

sys.stdin = open("input.txt", "rt")

t = int(input())
k = int(input())

coins = []

for i in range(k):
    a, b = map(int, input().split())
    for i in range(b):
        coins.append(a)

coins.sort(reverse=True)
total = sum(coins)

arr = []


def DFS(L, sums, res, tsum):
    if sums + total - tsum < t:
        return

    if sums > t:
        return

    if L == len(coins):

        if sums == t:
            arr.append([*res])
        res = []
    else:
        res.append(coins[L])
        DFS(L + 1, sums + coins[L], res, tsum + coins[L])
        res.pop()
        DFS(L + 1, sums, res, tsum + coins[L])


DFS(0, 0, [], 0)

arr = list(map((lambda v: str(v)), arr))
arr = set(arr)
print(len(arr))
