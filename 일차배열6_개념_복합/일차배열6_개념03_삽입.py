'''
    [문제]  
        a리스트가 있을 때, 리스트 사이에 값을 추가하고 
        나머지 값들은 뒤로 밀어내는 것을 삽입이라고 한다. 
        랜덤(0,6)으로 위치를 입력받고 
        a리스트 사이의 그 위치에 값 100을 삽입해 보시오.
    [예시]
        r = 3   
        a = [10,34,56,100,8,43]
'''

import random

a = [10,34,56,8,43]

r = random.randint(0, len(a))
print(r)

if r == len(a):
    a.append(100)
else:
    a.append(100)

    i = len(a) - 1
    while i > r:
        a[i] = a[i - 1]
        i -= 1
    a[r] = 100
    
print(a)
