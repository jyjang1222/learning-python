import random
'''
    [문제]
        숫자 10과 3을 각각 저장한다.
        랜덤으로 0~3 저장한다. 랜덤숫자는 연산자에 해당하고,
        각각의 숫자는 다른 연산자를 뜻한다. 
        (0 은 +, 1 은 -, 2는 *, 3은 / )
        숫자10과 3을 연산해주는 함수들과 식을 만드시오.
        위 식을 5번 반복하시오.
    [예시]
       r = 3
       3은 / 이므로 10 / 3 
'''
x = 10
y = 3

def plus():
    pass
def minus():
    pass
def multiply():
    pass
def divide():
    pass

def calc(r, a, b):
    calc = a + b
    operator = '+'
    if r == 1:
        calc = a - b
        operator = '-'
    elif r == 2:
        calc = a * b
        operator = '*'
    elif r == 3:
        calc = round(a / b, 2)
        operator = '/'
    res = calc
    print('r =', r, ',', a, operator, b, ' = ', res)

for i in range(5):
    r = random.randint(0, 3)
    calc(r, x, y)