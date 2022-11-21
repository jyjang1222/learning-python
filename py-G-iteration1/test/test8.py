import random

# 문제풀이1
# r = random.randint(1, 9)
# arr = []

# for i in range(6):
#     r = random.randint(1, 9)
#     arr.append(r)

# arr = [5, 7, 6, 2, 3, 1]
# tmp = arr[0]

# print(tmp, end = "")

# for i in range(1, len(arr)):
#     if i % 2 == 1:
#         print(" +", arr[i], end = "")
#         tmp += arr[i]
#     if i % 2 == 0:
#         print(" -", arr[i], end = "")
#         tmp -= arr[i]
#     if i == len(arr) - 1:
#         print()

# print(tmp)

# 문제풀이2
r = random.randint(1, 9)
prev = r
tmp = r

print(tmp, end = "")
for i in range(5):
    r2 = random.randint(1, 9)
    # 이전값 홀수짝수 조건식
    if prev % 2 == 1:
        print(" +", r2, end = "")
        tmp += r2
    if prev % 2 == 0:
        print(" -", r2, end = "")
        tmp -= r2
    # 이전값에 r2값 넣음
    prev = r2
    if i == 4:
        print()

print(tmp)

print()
# 정답
# i = 0
# op = 0
# r = random.randint(1, 9)
# if r % 2 == 1:
#         op = 1
# if r % 2 == 0:
#         op = 2
# total = r
# print(total , end=" ")
# while i < 5:
#         r = random.randint(1, 9)
#         if op == 1:
#                 print("+" , end=" ")
#                 total += r
#         if op == 2:
#                 print("-" , end=" ")
#                 total -= r
#         print(r , end=" ")
#         if r % 2 == 1:
#                 op = 1
#         if r % 2 == 0:
#                 op = 2
#         i += 1
# print("=" , total)