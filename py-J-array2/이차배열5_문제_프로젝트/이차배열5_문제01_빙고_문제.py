import random
'''
    [문제]
        철수는 빙고 게임을 만들고 있다.
        빙고 조건은 가로 1이 3개 또는 세로 1이 3개 또는 대각선으로 1이 3개이면 빙고이다.
        빙고는 중첩될 수 있다.
        반복적으로 랜덤 위치에 1을 저장한다. 
        단, 한번 1이 저장된 곳은 또 다시 저장할 수 없다.
        3빙고가 성립되면 종료한다. 
'''
bingo = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

while True:
    # 빙고판 세팅
    for i in range(len(bingo)):
        for j in range(len(bingo[i])):
            r = random.randint(0, 1)
            bingo[i][j] = r

    count = 0

    # 가로
    for i in range(len(bingo)):
        chk = True
        for j in range(len(bingo[i])):
            if bingo[i][j] != 1:
                chk = False
        if chk:
            count += 1

    # 세로
    # 001020 011121 021222
    for i in range(len(bingo)):
        chk = True
        for j in range(len(bingo[i])):
            if bingo[j][i] != 1:
                chk = False
        if chk:
            count += 1
    # 대각선
    # 001122 021120
    if bingo[0][0] == 1 and bingo[1][1] == 1 and bingo[2][2] == 1:
        count += 1
    if bingo[0][2] == 1 and bingo[1][1] == 1 and bingo[2][0] == 1:
        count += 1
    
    if count == 3:
        break


# 세팅된 빙고출력
for i in range(len(bingo)):
    print(bingo[i])