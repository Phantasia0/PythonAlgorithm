import sys

# sys.stdin = open("input.txt", "rt")

s = input()
stack = []
res = 0

for x in s:
    if x.isdecimal():
        stack.append(int(x))
    else:
        num1 = stack.pop()  # 뒤에
        num2 = stack.pop()  # 앞에

        if x == "+":
            res = num2 + num1
        elif x == "-":
            res = num2 - num1
        elif x == "*":
            res = num2 * num1
        elif x == "/":
            res = num2 / num1

        stack.append(res)

print(res)
