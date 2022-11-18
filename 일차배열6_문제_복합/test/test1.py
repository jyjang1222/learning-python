import random
"""
[문제]
    아래 리스트에 랜덤숫자 (1~30) 을  10개 저장한다. 
    단, 홀수만 저장하고 , 중복숫자는 없어야 한다. 
[예시]
    a = [29, 1, 5, 9 , 21, 25, 7, 3, 13, 15]

"""

a = []

while True:
    if len(a) == 10:
        break

    chk = True
    r = random.randint(1, 30)

    if r % 2 == 0:
        continue
    for i in range(len(a)):
        if a[i] == r:
            chk = False
    if chk:
        a.append(r)

print(a)