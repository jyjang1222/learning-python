import random
'''
[문제]
        50~100 사이의 랜덤값을 저장하고 그값의 약수를 전부 구하고, 
        그약수의 가운데 위치의 값만 출력한다. 
        만약에 약수의 개수가 짝수이면 가운데값 두개중 앞의 값을 출력한다. 
    [예시]
        50 => 1, 2, 5, 10, 25, 50 총 6개이므로 5 , 10 이 가운데 값들이고,  그 중 앞의 값 5를 출력한다. 
    [예시]
        51 => 1, 3, 17 총 3개 이므로 3만 출력한다. 
    [조건]
        배열을 쓰지 않고 풀어야한다.
'''

r = random.randint(50, 100)

약수갯수 = 0
count = 0
idx = 0

for i in range(1, r):
    if r % i == 0:
        약수갯수 += 1

if 약수갯수 % 2 == 0:
    idx = 약수갯수 // 2
if 약수갯수 % 2 == 1:
    idx = 약수갯수 // 2 + 1

for i in range(1, r):
    if r % i == 0:
        count += 1
        if count == idx:
            print(r, i)
    
for i in range(1, r):
    if r % i == 0:
        print(i, end = " ")
            



# 정답

# import random
# r = random.randint(50, 100)
# r = 50
# c = 0
# i = 1
# while i <= 50:
#     if r % i == 0:
#         c += 1
#         print(i)
#     i += 1

# print("------------------------------")
# print("c : " , c)
# center = 0
# if c % 2 == 1:
#     center = c // 2 + 1
# if c % 2 == 0:
#     center = c // 2 
# i = 1
# c2 =0
# while i <= 50:
#     if r % i == 0:
#         c2 += 1
#         if c2 == center:
#             print(i)
#     i += 1 
