import sys

# sys.stdin = open("input.txt", "rt")

l = int(input())
lines = list(map(int, input().split()))
m = int(input())

lines.sort()

for i in range(m):
    smallNum = lines.pop(0)
    smallNum += 1
    largeNum = lines.pop()
    largeNum -= 1

    lines.append(smallNum)
    lines.append(largeNum)
    lines.sort()


print(max(lines) - min(lines))
