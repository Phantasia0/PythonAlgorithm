"""
람다 함수
"""


# def plus_one(x):
#     return x + 1


# print(plus_one(1))
# 이것을 람다 함수로

# plus_two = lambda x: x + 1
# print(plus_two(1))
ranked_users = ["jon", "bob", "jane", "alice", "chris"]
user_details = list(
    map(lambda user: {"name": user[1], "rank": user[0]}, enumerate(ranked_users))
)
print(user_details)
a = [1, 2, 3]

print(list(map(lambda x: x + 1, a)))

queue = [(i, idx) for idx, i in enumerate(ranked_users)]
print(queue)
