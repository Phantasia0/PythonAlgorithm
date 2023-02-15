import sys

sys.stdin = open("input.txt", "rt")


def DFS(L, t, rsum):

    global maxX

    print(maxX, sum(res), t)

    if L == n:
        if t <= m:
            print("END", sum(res))
            sys.exit(0)
        else:
            return

    if t > m:
        temp = res.pop()
        if maxX < sum(res):
            maxX = sum(res)
        res.append(temp)
    elif t == m:
        if maxX < sum(res):
            maxX = sum(res)
    else:
        for i in range(1, n + 1):
            if check[i] == 0:
                check[i] = 1
                res.append(test[i].get("score"))
                DFS(L + 1, t + test[i].get("time"), rsum + test[i].get("score"))
                check[i] = 0
                res.pop()


n, m = map(int, input().split())

total = 0
test = {}
for i in range(1, n + 1):
    s, t = map(int, input().split())
    test[i] = {"score": s, "time": t}
    total += s

res = []
maxX = -2222222222
check = [0] * (n + 1)
DFS(0, 0, 0)
print(maxX)
