import sys

sys.stdin = open("input.txt", "rt")


def DFS(L, x):
    if L == 0:
        print(x - 1)
    else:
        if map[L][x - 1] == 0 and map[L][x + 1] == 0:
            if check[L - 1][x] == 0:
                check[L - 1][x] = 1
                DFS(L - 1, x)
        elif map[L][x - 1] == 0 and map[L][x + 1] == 1:
            if check[L][x + 1] == 0:
                check[L][x + 1] = 1
                DFS(L, x + 1)
            else:
                check[L - 1][x] = 1
                DFS(L - 1, x)
        elif map[L][x - 1] == 1 and map[L][x + 1] == 0:
            if check[L][x - 1] == 0:
                check[L][x - 1] = 1
                DFS(L, x - 1)
            else:
                check[L - 1][x] = 1
                DFS(L - 1, x)
        elif map[L][x - 1] == 1 and map[L][x + 1] == 1:
            if check[L][x - 1] == 0:
                check[L][x - 1] = 1
                DFS(L, x - 1)
            elif check[L][x + 1] == 0:
                check[L][x + 1] = 1
                DFS(L, x + 1)


dx = [1, -1]

map = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]

for i in range(10):
    map[i].insert(0, 0)
    map[i].append(0)

check = [[0] * 12 for _ in range(10)]

for idx, x in enumerate(map[9]):
    if x == 2:
        s = idx

check[9][s] = 1
DFS(9, s)
