import sys

sys.stdin = open("input.txt", "rt")

n = int(input())

hashMap = dict()
# hashMap = {}

for i in range(n):
    hashMap[input()] = 0

for i in range(n - 1):
    key = input()
    hashMap[key] = hashMap.get(key) + 1

# for key in hashMap:
for key, value in hashMap.items():
    if value == 0:
        print(key)
        break
