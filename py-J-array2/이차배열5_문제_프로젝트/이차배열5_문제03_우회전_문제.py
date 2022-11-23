import random
'''
    [문제]
        랜덤(1~4)를 저장한다. 랜덤숫자는 회전 횟수이다. 
        회전 횟수만큼 block의 숫자들을 90도로 우회전시키시오.
        
    [예시]
        rNum = 4
        1 2 3 
        4 5 6 
        7 8 9 

        7 4 1 
        8 5 2 
        9 6 3 

        9 8 7 
        6 5 4 
        3 2 1 

        3 6 9 
        2 5 8 
        1 4 7 
'''
block = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

r = random.randint(1, 4)

# 방법1
n = 1
if r % 4 == 1:
    for i in range(len(block) - 1, -1, -1):
        for j in range(len(block)):
            block[j][i] = n
            n += 1

n = 1
if r % 4 == 2:
    for i in range(len(block) - 1, -1, -1):
        for j in range(len(block) - 1, -1, -1):
            block[i][j] = n
            n += 1

n = 1
if r % 4 == 3:
    for i in range(len(block)):
        for j in range(len(block) - 1, -1, -1):
            block[j][i] = n
            n += 1


print(r)
for i in range(len(block)):
    print(block[i])
print()
# 방법2
print("# 방법2")
block = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(r)
for i in range(r):
    tmp = []
    for i in range(len(block)):
        tmp2 = []
        for j in range(len(block[i])):
            tmp2.append(block[i][j])
        tmp.append(tmp2)

    for i in range(len(block)):
        for j in range(len(block[i])):
            block[j][(len(block) - 1) - i] = tmp[i][j]

    for i in range(len(block)):
        print(block[i])
    print()