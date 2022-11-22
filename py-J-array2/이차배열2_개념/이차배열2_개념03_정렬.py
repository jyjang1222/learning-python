import random
'''
    [문제]
         a이차리스트에 값(1~100)을 9개 저장 후
         내림차순 정렬하시오.
    [예시]
        정렬 전 >>>
        [72, 23, 40]
        [67, 62, 88]
        [57, 54, 48]

        b = [72, 23, 40, 67, 62, 88, 57, 54, 48] 
        b :  [88, 72, 67, 62, 57, 54, 48, 40, 23]
        
        정렬 후 >>>
        [88, 72, 67]
        [62, 57, 54]
        [48, 40, 23]
'''
size = [3, 4, 3]
a = []

for i in range(3):
    tmp = []
    for j in range(size[i]):
        r = random.randint(1, 100)
        tmp.append(r)
    a.append(tmp)

print(a)


# 방법1
# tmp 에 넣을 idx 구하기
# 00 01 02 10 11 12 20 21 22
for i in range(len(a)):
    for j in range(len(a)):
        idx1 = i
        idx2 = j
        # print(idx1, idx2, end = " ")
        tmp = a[i][j]
        max = 0
        # 예) i = 0 j = 1 이라면
        # max 찾기1 
        # 0 1, 0 2 체크. 전의 0 0 은 제외
        for k in range(j, len(a)):
            if a[i][k] > max:
                max = a[i][k]
                idx3 = i
                idx4 = k
        # max 찾기2
        # 1 0, 1 1, 1 2, 2 0, 2 1, 2 2 체크 
        for k in range(i + 1, len(a)):
            for m in range(len(a)):
                if a[k][m] > max:
                    max = a[k][m]
                    idx3 = k
                    idx4 = m
        
        # print(tmp,idx1,idx2,idx3,idx4,max)
        a[idx1][idx2] = a[idx3][idx4]
        a[idx3][idx4] = tmp

print(a)
print()


# 방법2
a = []

for i in range(3):
    tmp = []
    for j in range(size[i]):
        r = random.randint(1, 100)
        tmp.append(r)
    a.append(tmp)

print(a)

# 일차에 모두 넣은후에 이차로 다시 만들자
b = []

for i in range(len(a)):
    for j in range(len(a[i])):
        b.append(a[i][j])

print(b)

# 정렬

for i in range(len(b)):
    tmp = b[i]
    max = b[i]
    maxIdx = i
    for j in range(i, len(b)):
        if b[j] > max:
            max = b[j]
            maxIdx = j
    b[i] = b[maxIdx]
    b[maxIdx] = tmp

print(b)

c = []
n = 0
for i in range(3):
    tmp = []
    for j in range(size[i]):
        tmp.append(b[n])
        n += 1
    c.append(tmp)

print(c)



# a = [
#         [0,0,0],
#         [0,0,0],
#         [0,0,0]
#     ]

# for i in range(len(a)):
#     for j in range(len(a[i])):
#         a[i][j] = random.randint(1,100)
        
# print("정렬 전 >>>")
# for i in range(len(a)):
#     print(a[i])

# b = []
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         b.append(a[i][j])
# print("b =", b)

# i = 0
# while i < len(b):
#     max = b[i]
#     maxIndex = i

#     j = i
#     while j < len(b):
#         if max < b[j]:
#             max = b[j]
#             maxIndex = j
#         j += 1
    
#     temp = b[i]
#     b[i] = b[maxIndex]
#     b[maxIndex] = temp

#     i += 1
# print("b : " , b)

# index = 0
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         a[i][j] = b[index]
#         index += 1
# print("정렬 후 >>>")
# for i in range(len(a)):
#     print(a[i])
