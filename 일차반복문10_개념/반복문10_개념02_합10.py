import random
'''
[문제]
    1~9 사이의 랜덤 숫자 2개를 저장하고
    그 숫자의 합이 무조건 10이 되도록 출력하시오.
[예시]
    x = 9
    y = 1
'''

# 풀이
num1 = 0
num2 = 0

while True:
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    sum = num1 + num2
    if sum == 10:
        print(num1, num2, sum)
        break














# x = 0
# y = 0

# run = 1
# while run == 1:
#     x = random.randint(1, 9)
#     y = random.randint(1, 9)

#     total = x + y
#     if total == 10:
#         run = 0
# print("x =", x)
# print("y =", y)


