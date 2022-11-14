'''
    [문제]
        10~100 사이의 랜덤 숫자를 다섯 개 저장한다. 
        각 숫자의 약수를 전부 출력한다. 
    
    [예시]    
        52 : 1 2 4 13 26 52 
        81 : 1 3 9 27 81 
        28 : 1 2 4 7 14 28
        11 : 1 11
        52 : 1 2 4 13 26 52
'''
import random

arr = []

for i in range(5):
    r = random.randint(10, 100)
    arr.append(r)

print(arr)

for i in arr:
    print(i, end = ":")
    j = 1
    while True:
        if i % j == 0:
            print(j, end = " ")
        if j == i:
            break
        j += 1
    print()









# for i in range(5):
#     r = random.randint(10, 100)
#     print(r, end=" : ")

#     for j in range(r):
#         if r % (j + 1) == 0:
#             print(j + 1, end=" ")
#     print()
