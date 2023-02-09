import sys

sys.stdin = open("input.txt", "r")

str = input()

str = list(filter(lambda char: char.isalpha() != True, str))
str = "".join(str)
num = int(str)

cnt = 0
for i in range(1, num + 1):
    if num % i == 0:
        cnt += 1

print(num)
print(cnt)

# for char in str:
#     if char.isalpha():
#         print(char)
