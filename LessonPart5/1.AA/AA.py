import sys

sys.stdin = open("input.txt", "rt")

n = int(input())


def DFS(n):
    res = []
    if n == 0:
        return res

    cnt = 0
    num = n
    while num > 1:
        num = num // 2
        cnt += 1

    res.append(cnt)
    res.extend(DFS(n - 2 ** (cnt)))
    return res


res = DFS(n)

answer = [0] * (res[0] + 1)
for value in res:
    answer[len(answer) - 1 - value] = 1

print("".join([str(i) for i in answer]))

# 재귀함수...이해하고 적용하기 위해서 2시간걸림..
