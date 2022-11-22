import random
'''
    [문제]
         a이차리스트에 10~90까지 값을 저장 후 셔플하시오.
    [예시]
        셔플 전 >>>
        [10, 20, 30]
        [40, 50, 60]
        [70, 80, 90]
        
        셔플 후 >>> 
        [40, 20, 80]
        [10, 60, 90]
        [30, 70, 50]    
'''

# bonus 1차배열 셔플 연습
lotto = []

for i in range(1, 46):
    lotto.append(i)

i = 0
while i <= 100:
    r1 = random.randint(0, len(lotto) - 1)
    r2 = random.randint(0, len(lotto) - 1)
    tmp = lotto[r1]
    lotto[r1] = lotto[r2]
    lotto[r2] = tmp
    i += 1

for i in range(6):
    print(lotto[i], end = " ")
print()

# 문제풀이
a = []
n = 10

for i in range(3):
    tmp = []
    for j in range(3):
        tmp.append(n)
        n += 10
    a.append(tmp)

print(a)

i = 0
while i <= 100:
    r1 = random.randint(0, len(a) - 1)
    r2 = random.randint(0, len(a[0]) - 1)
    r3 = random.randint(0, len(a) - 1)
    r4 = random.randint(0, len(a[0]) - 1)
    tmp = a[r1][r2]
    a[r1][r2] = a[r3][r4]
    a[r3][r4] = tmp
    i += 1

print(a)











# a = [
#         [0,0,0],
#         [0,0,0],
#         [0,0,0]
#     ]

# b = [10,20,30,40,50,60,70,80,90]

# index = 0
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         a[i][j] = b[index]
#         index += 1

# print("셔플 전 >>>")
# for i in range(len(a)):
#     print(a[i])

# for i in range(1000):
#     r1 = random.randint(0, 2)
#     r2 = random.randint(0, 2)
#     temp = a[r1][r2]
#     a[r1][r2] = a[0][0]
#     a[0][0] = temp
    
# print("셔플 후 >>>")
# for i in range(len(a)):
#     print(a[i])

