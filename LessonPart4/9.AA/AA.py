import sys

# sys.stdin = open("input.txt", "rt")

s1 = input()
s2 = input()

hashMap1 = {}
hashMap2 = {}


def finding(string):
    hashMap = {}
    for i in range(len(string)):
        if string[i] not in hashMap:
            hashMap[string[i]] = 1
        else:
            hashMap[string[i]] = hashMap.get(string[i]) + 1

    return hashMap


hashMap1 = finding(s1)
hashMap2 = finding(s2)

cnt = 0
isConfirm = True
for keyI, valueI in hashMap1.items():
    if isConfirm == False:
        print("NO")
        break

    for keyJ, valueJ in hashMap2.items():
        if keyI == keyJ:
            if valueI != valueJ:
                isConfirm = False
                break
            else:
                cnt += 1
else:
    if cnt == len(hashMap1.keys()) and cnt == len(hashMap2.keys()):
        print("YES")
    else:
        print("NO")
