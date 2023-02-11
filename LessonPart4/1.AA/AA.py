import sys

# sys.stdin = open("input.txt", "rt")

num, k = map(int, (input().split()))

num = str(num)
numList = [int(num[i]) for i in range(len(num))]


stack = []
stack.append(numList[0])

for i in range(1, len(numList)):

    while True:
        if len(stack) == 0:
            break

        if stack[len(stack) - 1] < numList[i]:
            if k <= 0:
                break
            stack.pop()
            k -= 1
        else:
            break

    stack.append(numList[i])

for i in range(k):
    stack.pop()

for i in range(len(stack)):
    stack[i] = str(stack[i])

result = "".join(stack)
print(result)
