'''
    [문제]
        a리스트와 b리스트를 비교해서 서로 겹치는 값을 0으로 변경하시오.
    [정답] 
        a = [
                [0, 0, 0],
                [0, 7, 2]
            ] 
        b = [0, 6, 0, 0, 0]
'''

a = [[1,4,3],[5,7,1]]
b = [4,6,3,1,5]

a2 = []
for i in range(len(a)):
    for j in range(len(a[i])):
        a2.append(a[i][j])

print("a2:", a2)

n = 0
for i in a2:
    for j in b:
        # 같은수 n에 넣기
        if i == j:
            n = i
        # a2에 n과 같은수 0넣기
        for k in range(len(a2)):
            if a2[k] == n:
                a2[k] = 0
        # b에 n과 같은수 0넣기
        for m in range(len(b)):
            if b[m] == n:
                b[m] = 0

print("a2:", a2)
print("b:", b)
c = []
n = 0
for i in range(len(a)):
    tmp = []
    for j in range(len(a[i])):
        tmp.append(a2[n])
        n += 1
    c.append(tmp)

a = c

print("a2:", a)
print("b:", b)












# for i in range(len(b)):

#     for j in range(len(a)):
#         for k in range(len(a[j])):
#             if b[i] == a[j][k]:
#                 a[j][k] = 0
#                 b[i] = 0
# for i in range(len(a)):
#     print(a[i])
# print(b)