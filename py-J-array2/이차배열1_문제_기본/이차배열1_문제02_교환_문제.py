import random
'''
    [문제]
        [1] a이차리스트에 랜덤 값(1~100)을 9개 저장 후 출력하시오.
        [2] 랜덤으로 값 두 개를 선택 후 두 개의 위치를 교환 후 출력하시오.
    [예시]
    값 교체 전 >>>
    [46, 62, 75]
    [36, 18, 100]
    [26, 11, 39]

    r1 = 11
    r2 = 36
    
    값 교체 후 >>>
    [46, 62, 75]
    [11, 18, 100]
    [26, 36, 39]
'''
a = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(len(a)):
    for j in range(len(a[i])):
        r = random.randint(1, 100)
        a[i][j] = r

print(a)

n1 = random.randint(0, len(a) - 1)
n2 = random.randint(0, len(a[0]) - 1)
n3 = random.randint(0, len(a) - 1)
n4 = random.randint(0, len(a[0]) - 1)
tmp = 0
print(n1, n2, a[n1][n2])
print(n3, n4, a[n3][n4])
tmp = a[n1][n2]
a[n1][n2] = a[n3][n4]
a[n3][n4] = tmp

print(a)
