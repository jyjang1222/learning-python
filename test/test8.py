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