import sys

sys.stdin = open("input.txt", "rt")

testCase = int(input())
for i in range(testCase):
    n, s, e, k = map(int, input().split())
    nums = list(map(int, input().split()))

    new = nums[s - 1 : e]
    new.sort()
    print(new)
    print("{}{} {}".format("#", i + 1, new[k - 1]))
