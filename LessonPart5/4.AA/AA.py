import sys

sys.stdin = open("input.txt", "rt")


def DFS(s):
    cnt = nums[s]
    if cnt == 0:
        sum = 0
        for i in range(1, max(nums) + 1):
            if check[i] == 1:
                sum += i
        if sum == total / 2:
            isTrue.append(1)
        else:
            isTrue.append(0)
    else:
        check[cnt] = 1
        DFS(s + 1)
        check[cnt] = 0
        DFS(s + 1)


n = int(input())
nums = list(map(int, input().split()))
nums.append(0)
isTrue = []

check = [0] * (max(nums) + 1)
total = sum(nums)
if total % 2 != 0:
    print("NO")
else:
    DFS(0)
    if sum(isTrue) >= 1:
        print("YES")
    else:
        print("NO")
