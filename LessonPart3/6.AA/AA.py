import sys

# sys.stdin = open("input.txt", "rt")

n = int(input())
list = []

for i in range(n):
    height, weight = map(int, input().split())
    list.append((height, weight))

list.sort(key=lambda x: (-x[0], -x[1]))

res = []
stdH = 0
stdW = 0
cnt = 0
for height, weight in list:
    if height < stdH and weight < stdW:
        continue
    else:
        res.append((height, weight))
        cnt += 1
        stdH = res[len(res) - 1][0]
        stdW = res[len(res) - 1][1]

print(cnt)
