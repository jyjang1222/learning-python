'''
    [문제]
        a리스트와 b리스트를 비교해서 서로 겹치는 값을 0으로 변경하시오.
    [정답] 
    a = [
            [0, 4, 0],
            [0, 0, 0]
        ]
    b = [
            [0, 0, 0],
            [0, 0, 8]    
        ]
'''

a = [[1,4,3],[5,7,2]]
b = [[5,3,2],[1,7,8]]

a2 = []
b2 = []
for i in range(len(a)):
    for j in range(len(a[i])):
        a2.append(a[i][j])
        b2.append(b[i][j])

print("a2:", a2)
print("b2:", b2)

n = 0
for i in a2:
    for j in b2:
        # 같은수 n에 넣기
        if i == j:
            n = i
        # a2에 n과 같은수 0넣기
        for k in range(len(a2)):
            if a2[k] == n:
                a2[k] = 0
        # b2에 n과 같은수 0넣기
        for m in range(len(b2)):
            if b2[m] == n:
                b2[m] = 0

print("a2:", a2)
print("b2:", b2)

c = []
d = []

n = 0
for i in range(len(a)):
    tmp = []
    tmp2 = []
    for j in range(len(a[i])):
        tmp.append(a2[n])
        tmp2.append(b2[n])
        n += 1
    c.append(tmp)
    d.append(tmp2)

a = c
b = d

print("a:", a)
print("b:", b)









# for i in range(len(a)):
#     for j in range(len(a[i])):

#         for y in range(len(b)):
#             for x in range(len(b[y])):
#                 if a[i][j] == b[y][x]:
#                     a[i][j] = 0
#                     b[y][x] = 0

# for i in range(len(a)):
#     print(a[i])
# print()

# for i in range(len(b)):
#     print(b[i])