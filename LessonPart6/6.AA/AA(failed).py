import sys

sys.stdin = open("input.txt", "rt")


def DFS(L, str,res):

    if int(str) > 27:
        return

    global cnt
    if L == len(s):
        cnt += 1
    else:
        res.append(str)
        DFS(L+1,str+s[L], res)



s = input()
strings = []
cnt = 0

hashMap = {}
for i in range(1, 27):
    hashMap[i] = chr(ord("A") + i - 1)

DFS(0,0)
