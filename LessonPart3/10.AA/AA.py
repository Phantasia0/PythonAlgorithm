import sys

sys.stdin = open("input.txt", "rt")

n = int(input())
nums = list(map(int, input().split()))

res = []
cnt = 0
idx = -1
while len(res) < n:
    for i in range(idx + 1, n):
        if nums[i] == cnt:
            res.append(i + 1)
            idx = i
            break
    else:
        cnt += 1
        idx = -1
    count = 0
    if idx != -1:
        for i in range(len(res) - 1):
            if res[i] > res[len(res) - 1]:
                count += 1
        count = count - nums[idx]
        temp = res.pop()
        if count == 0:
            res.append(temp)
        else:
            res.insert(-count, temp)


for i in res:
    print(i, end=" ")

