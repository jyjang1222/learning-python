import random

'''
        [문제]
            랜덤 숫자(1~4)를 입력받고 그숫자만큼 앞으로 값들을 회전시키시오.
            회전이란 다음과 같다.
            1회전 [1,2,3,4,5] => [2,3,4,5,1]
            2회전 [1,2,3,4,5] => [3,4,5,1,2]
            3회전 [1,2,3,4,5] => [4,5,1,2,3]
            4회전 [1,2,3,4,5] => [5,1,2,3,4]
        [예시]
            r = 4  
            [1,2,3,4,5] => [5,1,2,3,4]
'''

r = random.randint(1, 4)
# r = 1
print(r)

a = [1, 2, 3, 4, 5]

tmp = 0 

for j in range(r):
    tmp = a[0]
    for i in range(len(a) - 1):
        a[i] = a[i + 1]
    a[len(a) - 1] = tmp   

# for k in range(1, r + 1):
#     a[len(a) - r - 1 + k] = k

print(a)


# 정답
a = [1,2,3,4,5]

print('r =', r)
for i in range(len(a)):
    a[i] += r
    if a[i] > 5:
        a[i] -= len(a)
print('a =', a)


# 학생풀이1
a = [1,2,3,4,5]

for i in range(r):
    t = a[0]
    for j in range(len(a) - 1):
        a[j] = a[j + 1]
    a[-1] = t

print(a)