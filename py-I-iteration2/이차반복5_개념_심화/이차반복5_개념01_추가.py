import random
'''
    [문제]
        a리스트에는 이미 1~3의 값이 저장되어 있다.
        이제 추가로 랜덤(1~10)을 10번 추가하려 한다. 
        단, 중복숫자가 있으면 저장하지 않는다.
    [예시]
        [1, 2, 3, 10, 8, 9, 4]
'''

a = [1,2,3]


for i in range(10):
    r = random.randint(1, 10)
    chk = True
    for j in range(len(a)):
        if a[j] == r:
            chk = False
    if chk:
        a.append(r)
        print(r)
    else:
        print(r, "중복숫자")
    print(a)


















# i = 0
# while i < 10:
#     r = random.randint(1, 10)

#     check = False
#     j = 0
#     while j < len(a):
#         if r == a[j]:
#             check = True
#             break
#         j += 1
    
#     if check == False:
#         a.append(r)
#     i += 1

# print(a)


