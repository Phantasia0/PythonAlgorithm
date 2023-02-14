import sys

sys.stdin = open("input.txt", "rt")


def DFS(L, sum):
    global min
    if L > min:
        return

    if sum > m:
        return

    if sum == m:
        if L < min:
            min = L
    else:
        for i in range(n):
            DFS(L + 1, sum + coins[i])


n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
m = int(input())
min = 22222222


DFS(0, 0)
print(min)
