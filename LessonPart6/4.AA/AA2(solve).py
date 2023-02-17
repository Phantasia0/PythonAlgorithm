import sys

# sys.stdin = open("input.txt", "rt")

t = int(input())
k = int(input())

coins = {}

for i in range(k):
    a, b = map(int, input().split())
    coins[a] = b

total = sum(coins)

cnt = 0

nums = list(coins.keys())
counts = list(coins.values())


def DFS(L, sums):
    global cnt

    if sums > t:
        return

    if L == k:
        if sums == t:
            cnt += 1
    else:
        for i in range(counts[L] + 1):
            DFS(L + 1, sums + (nums[L] * i))


DFS(0, 0)
print(cnt)
