import random
# # 1

# r = random.randint(3, 8)
# # r = 5
# # r = 4
# # 10^r ~ 10^(r+1) - 1
# i = 1
# j = 1
# while i < r:
#     j *= 10
#     i += 1

# print(r, j)

# r2 = random.randint(j, j * 10 - 1)
# # r2 = 61410
# # r2 = 6031
# print(r2)

# a = r // 2 + 1
# i = 1
# j = 1
# while i <= a:
#     j *= 10
#     i += 1
# print(j)
# print(r2 % j)
# 자리홀수
# if r % 2 == 1:
# print((r2 % j) // (j // 10))
# 자리짝수
# if r % 2 == 0:
    # print((r2 % j) // (j // 10))



# 학생풀이1
# digits = random.randint(3, 8)
# print("digits =", digits)

# start = 10 ** (digits - 1)
# end = 10 ** digits - 1

# num = random.randint(start, end)
# print("num =", num)

# if digits % 2 != 0:
#     i = 1
#     j = digits // 2
#     while j >= 1:
#         num %= 10 ** (digits - i)
#         j -= 1
#         i += 1
#     result = num // 10 ** (digits - i)
# if digits % 2 == 0:
#     i = 1
#     j = digits // 2 - 1
#     while j >= 1:
#         num %= 10 ** (digits - i)
#         j -= 1
#         i += 1
#     result = num // 10 ** (digits - i)

# print(result)

# 2
r = random.randint(3, 8)

i = 1
for j in range(r - 1):
    i *= 10
r2 = random.randint(i, i * 10 - 1)
# r = 6
# r2 = 220222
print(r, r2)

pos = r // 2 + 1

n = 0
for i in range(pos):
    n = r2 % 10
    r2 //= 10

print(n)





# 정답
# import random
# i = 1
# a = 1
# while i < r:
#     a *= 10
#     i += 1

# b = a * 10 - 1
# print(r , a, b)
# center = 0
# if r % 2 == 1:
#     center = r // 2 + 1
# else:
#     center = r // 2

# print("center : " , center)
# r2 = random.randint(a, b)
# print("rand : " , r2)
# run = 1
# i = r  # 자리수는 뒤에서 부터 구한다. 
# while run == 1:
#     temp = r2 % 10
#     r2 //= 10
#     if i == center:
#         print("중앙값 : " , temp)
#         run = 0
#     i -= 1