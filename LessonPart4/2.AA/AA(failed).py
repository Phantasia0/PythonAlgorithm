import sys

sys.stdin = open("input.txt", "rt")

lines = input()

result = [lines[0]]
for i in range(1, len(lines)):
    if lines[i - 1] == "(" and lines[i] == ")":
        result.pop()
        result.append("@")
        continue
    result.append(lines[i])

print(result)
stack = []
cnt = 0
final = 0
finalList = []
for i in range(len(result)):
    if result[i] == "(":
        cnt += 1
        stack.append(result[i])

    elif result[i] == ")":
        cnt -= 1
        stack.pop()
    else:
        if len(stack) != 0:
            final = cnt + 1
            finalList.append(final)

    if len(stack) == 0:
        cnt = 0

sum = sum(finalList)
print(sum)
