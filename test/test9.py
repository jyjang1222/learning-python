import random
# 1

r = random.randint(3, 8)
# r = 5
# r = 4
# 10^r ~ 10^(r+1) - 1
i = 1
j = 1
while i < r:
    j *= 10
    i += 1

print(r, j)

r2 = random.randint(j, j * 10 - 1)
# r2 = 61410
# r2 = 6031
print(r2)

a = r // 2 + 1
i = 1
j = 1
while i <= a:
    j *= 10
    i += 1
print(j)
# print(r2 % j)
# 자리홀수
# if r % 2 == 1:
print((r2 % j) // (j // 10))
# 자리짝수
# if r % 2 == 0:
    # print((r2 % j) // (j // 10))











# 정답
# r = random.randint(3,8)
# i = 1
# a = 1
# size = 0
# while i < r:
#     a *= 10
#     size += 1
#     i += 1

# b = a * 10 - 1
# print(r , a, b, size)
# center = 0
# if size % 2 == 1:
#     center = size // 2 + 1
# else:
#     center = size //2 

# print("center : " , center)
# r = random.randint(a, b)
# print("rand : " , r)
# run = 1
# i = 0
# while run == 1:
#     temp = r % 10
#     if i == center:
#         print("중앙값 : " , temp)
#         run = 0
#     r //= 10
#     i += 1