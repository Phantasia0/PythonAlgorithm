import sys

# sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())

result = []
count = []

for i in range(1, N + 1):
    for j in range(1, M + 1):
        result.append(i + j)

result = list(map(lambda x: [x, result.count(x)], result))
[count.append(x) for x in result if x not in count]
count.sort(key=lambda x: (-x[1], x[0]))
count = list(filter(lambda x: x[1] == count[0][1], count))

for value in count:
    print(value[0], end=" ")
