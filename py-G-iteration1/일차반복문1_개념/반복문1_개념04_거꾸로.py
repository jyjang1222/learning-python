'''
[문제] 4~1 까지 거꾸로 출력하시오.
[정답] 4 3 2 1
'''

i = 4
while i >= 1:
    print(i)
    i -= 1

'''
위 방법보다는 아래 방법을 권장한다.
반복 횟수를 파악하는데 아래 방법이 더 직관적이다.
추가로 변수를 선언해서 원하는 값을 얻으면 된다. 

'''
print("====================")

i = 1
num = 4

while i <= 4:
    print(num)
    num -= 1
    i += 1

# while문 연습

j = 6
while j >= 2:
    print(j)
    j -= 1
    # 65432
    

k = 6
j = 2

while j <= 6:
    print(num)
    # 65432
    j += 1
    k -= 1