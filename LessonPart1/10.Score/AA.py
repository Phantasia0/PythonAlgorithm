import sys

sys.stdin = open("input.txt", "r")

n = int(input())
checks = list(map(int, input().split()))
score = 0
cnt = 0
for check in checks:
    if check == 1:
        cnt = cnt + 1
        score += cnt
    else:
        cnt = 0

print(score)
