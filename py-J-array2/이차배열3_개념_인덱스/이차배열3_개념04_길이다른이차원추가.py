'''
    [문제]
        철수는 창고정리를 하고 있다.
        숫자는 물품번호를 뜻하고, 이를 이차원배열에 저장한다.
        철수는 정신없이 물건을 나열하면서 이차원 구획은 0으로 표시를 해놓았다.
        단, 0은 구획이기 때문에 추가하지 않는다. 
        아래 예시를 참고하시오.
    [예시]
        3,14,11,12,0 (여기가 구획이다),
        232,22,234,0 (여기가 구획이다),
        24,14,34,44,54,63,33,63,0, (여기가 구획이다),
        4,32,3
    [정답]
    b = [
            [13, 14, 11, 12]
            [232, 22, 234]
            [24, 14, 34, 44, 54, 63, 33, 63]
            [4, 32, 3]
        ]
'''

a = [13,14,11,12,0,232,22,234,0,24,14,34,44,54,63,33,63,0,4,32,3]
b = []		    


tmp = []
for i in a:
    if i != 0:
        tmp.append(i)
    if i == 0 or i == a[len(a) - 1]:
        b.append(tmp)
        tmp = []
    # print(i, tmp)

print(b)



b = []
tmp = []
for i in a:
    if i != 0:
        tmp.append(i)
    elif i == 0:
        b.append(tmp)
        tmp = []

    if i == a[len(a) - 1]:
        b.append(tmp)
        tmp = []

print(b)











# temp = []
# for i in range(len(a)):
#     if a[i] != 0:
#         temp.append(a[i])
#     else:
#         b.append(temp)
#         temp = [] 

#     if i == len(a) - 1:   
#         b.append(temp)

# for i in range(len(b)):
#     print(b[i])
