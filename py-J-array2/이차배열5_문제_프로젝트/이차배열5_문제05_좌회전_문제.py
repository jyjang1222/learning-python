import random
'''
    [문제]
        랜덤(1~4)를 저장한다. 랜덤숫자는 회전 횟수이다. 
        회전 횟수만큼 block의 숫자들을 90도로 좌회전시키시오.
    [예시]
        rNum = 4
        1 2 3 
        4 5 6 
        7 8 9 

        3 6 9 
        2 5 8 
        1 4 7 

        9 8 7 
        6 5 4 
        3 2 1 

        7 4 1 
        8 5 2 
        9 6 3 
'''
block = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(block)):
    print(block[i])

r = random.randint(1, 4)
# r = 2
print(r)

for i in range(r):
    # 배열은 참조형이기 때문에 원본 복사
    tmp = []
    for i in range(len(block)):
        tmp2 = []
        for j in range(len(block)):
            tmp2.append(block[i][j])
        tmp.append(tmp2)

    # for i in range(len(tmp)):
    #     print(tmp[i])
    # 회전
    for i in range(len(tmp)):
        for j in range(len(tmp)):
            block[2-j][i] = tmp[i][j]

    # 출력
    for i in range(len(block)):
        print(block[i])
    print()