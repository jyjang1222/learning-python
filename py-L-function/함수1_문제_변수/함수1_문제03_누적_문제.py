import random
'''
    [문제]
        1~10 사이의 숫자를 랜덤으로 2개 저장하고,
        작은 숫자부터 큰 숫자까지의 합을 출력하는 함수를 만드시오.
    [예시]
        5, 3 ==> 3 + 4 + 5 = 12
        2, 6 ==> 2 + 3 + 4 + 5 + 6 = 20
'''

r1 = random.randint(1, 10)
r2 = random.randint(1, 10)
print(r1, r2)

def sum(n1, n2):
    if n1 > n2:
        tmp = n1
        n1 = n2
        n2 = tmp
    sum = 0
    for i in range(n1, n2 + 1):
        print(sum, end = " ")
        sum += i
        print('+', i)
    print(sum)

sum(r1, r2)