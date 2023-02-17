import sys

# sys.stdin = open("input.txt", "rt")


def DFS(L, aSum, bSum, cSum):
    global mins

    if L == n:
        if aSum != bSum and bSum != cSum and aSum != cSum:
            lists = [aSum, bSum, cSum]
            temp = max(lists) - min(lists)
            if temp < mins:
                mins = temp
    else:
        DFS(L + 1, aSum + cv[L], bSum, cSum)
        DFS(L + 1, aSum, bSum + cv[L], cSum)
        DFS(L + 1, aSum, bSum, cSum + cv[L])


n = int(input())

cv = list()
for i in range(n):
    cv.append(int(input()))

mins = 222222222222
DFS(0, 0, 0, 0)
print(mins)
