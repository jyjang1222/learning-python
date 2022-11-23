'''
    [문제]
        a리스트와 b리스트를 비교해서 
        서로 겹치는 값을 0으로 변경하시오.
        중복되는 값은 전부 0으로 변경한다.
    [정답]
    a = [
            [0, 4, 0],
            [0, 0, 0],
            [0, 4, 0]
        ]
    b = [
            [0, 0, 0],
            [0, 0, 8],
            [6, 0, 0]
        ]
'''

a = [[1,4,3],[5,7,2],[5,4,1]]
b = [[5,3,2],[1,7,8],[6,5,1]]

a2 = []
b2 = []

for i in range(len(a)):
    for j in range(len(a[i])):
        a2.append(a[i][j])
        b2.append(b[i][j])

# print(a2)
# print(b2)

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

print(a2)
print(b2)

def tie(arr):
    res = []
    tmp = []
    for i in range(len(arr)):
        tmp.append(arr[i])
        if i % 3 == 2:
            res.append(tmp)
            tmp = []
    return res

res1 = tie(a2)
res2 = tie(b2)
print(res1)
print(res2)