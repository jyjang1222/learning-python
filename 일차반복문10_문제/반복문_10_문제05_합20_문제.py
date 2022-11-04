import random

'''
    [문제]
        1~10 사이의 랜덤 숫자 3개 저장하고
        그 숫자의 합이 무조건 20이 되도록 출력해보자.
'''

sum = 0

while True:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    num3 = random.randint(1, 10)

    sum = num1 + num2 + num3
    if sum == 20:
        print(num1, num2, num3, sum)
        break