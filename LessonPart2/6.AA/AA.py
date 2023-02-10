import sys

sys.stdin = open("input.txt", "rt")

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

sum = 0
res = []
for idxX, _ in enumerate(array):
    for idxY, _ in enumerate(array):
        sum += array[idxX][idxY]
    res.append(sum)
    sum = 0

for idxY, _ in enumerate(array):
    for idxX, _ in enumerate(array):
        sum += array[idxX][idxY]
    res.append(sum)
    sum = 0

for idxX, _ in enumerate(array):
    sum += array[idxX][idxX]
else:
    res.append(sum)
    sum = 0

for idxX, _ in enumerate(array):
    sum += array[idxX][len(array) - 1 - idxX]
else:
    res.append(sum)
    sum = 0

number = max(res)
print(number)
