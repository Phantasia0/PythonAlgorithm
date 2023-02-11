import sys

sys.stdin = open("input.txt", "rt")

n = int(input())
se = [list(map(int, input().split())) for _ in range(n)]

se.sort(key=lambda x: (x[1],x[0]))
res = []

res.append(se[0])
for i in se:
    startTime = i[0]
    if startTime >= res[len(res) - 1][1]:
        res.append(i)

print(len(res))
