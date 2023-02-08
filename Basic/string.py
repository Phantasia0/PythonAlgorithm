"""
문자열과 내장함수
"""
msg = "It is Time"
print(msg.upper())
print(msg.lower())
print(msg)
tmp = msg.upper()
print(tmp)
print(tmp.find("T"))
print(tmp.count("T"))
print(msg[:2])
print(msg[3:5])
print(len(msg))
# for i in range(len(msg)):
#     print(msg[i], end="")

# for value, index in enumerate(msg):
#     print(value, index)

# for x in msg:
#     print(x, end=" ")
# print()

# for char in msg:
#     if char.isupper():
#         print(char, end=" ")

# for char in msg:
#     if char.islower():
#         print(char, end=" ")

for char in msg:
    if char.isalpha():
        print(char, end="")
print()

tmp = "az"
for x in tmp:
    print(ord(x))

tmp = 65
print(chr(tmp))
