import random
'''
    [문제]
         a 이차리스트에 10~90까지 값을 저장 후
         랜덤으로 값 하나를 출력하시오.
    [예시]
        a :  [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
        r1 : 1  r2 : 0
        40
'''
# 1 
# 초기화후에 넣기
a = []

for i in range(3):
    tmp = []
    for j in range(3):
        tmp.append(0)
    a.append(tmp)

print(a)

n = 10
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = n
        n += 10

print(a)

# 2
# 넣으면서 초기화
a = []
n = 10
for i in range(3):
    tmp = []
    for j in range(3):
        tmp.append(n)
        n += 10
    a.append(tmp)

print(a)














# a = [
#         [0,0,0],
#         [0,0,0],
#         [0,0,0]
#     ]

# print("a : " , a)

# k = 1
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         a[i][j] = k * 10
#         k += 1
# print("a : " , a)

# 이차원이므로 인덱스 2개 필요하다. 
# r1 = random.randint(0, 2)
# r2 = random.randint(0, 2)
# print("r1 :", r1 , " r2 :", r2)
# print(a[r1][r2])




