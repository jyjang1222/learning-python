import random
'''
    [문제]
        [조건1] a, b 리스트 두 개에 1~100 사이의 랜덤 값 다섯 개를 저장한다.
        [조건2] base 변수에 랜덤으로 1~100 사이의 숫자를 저장한다. 
        base 변수값보다 큰 값들을 전부 출력하시오.
    [예시]
'''

a = []
b = []

base = random.randint(1, 100)


for i in range(5):
    num = random.randint(1, 100)
    a.append(num)
    num = random.randint(1, 100)
    b.append(num)

    if a[i] > base:
        print(a[i], ">", base)
    if b[i] > base:
        print(b[i], ">", base)

print(a)
print(b)

