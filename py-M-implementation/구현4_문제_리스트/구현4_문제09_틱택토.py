"""
[틱택토]
    조건1) 구글 크롬에 "틱택토" 검색후 게임을 한번하고 
                아래와같이 만들어보기.
    조건2) P1 , P2 를 플레이어가 번갈아가면서 플레이.
    조건3) 먼저 한줄을 완성하면 승리
    =============
    [처음화면]
    0,0,0
    0,0,0
    0,0,0
    [p1]인덱스 입력 : 6
    =============
    [1턴]
    0,0,0
    0,0,0
    1,0,0
    [p2]인덱스 입력 : 1
    =============
    [2턴]
    0,2,0
    0,0,0
    1,0,0
    [p1]인덱스 입력 : 3
    =============
    [3턴]
    0,2,0
    1,0,0
    1,0,0
    [p2]인덱스 입력 : 2
    =============
    [4턴]
    0,2,2
    1,0,0
    1,0,0
    [p1]인덱스 입력 : 0
    =============
    [5턴]
    1,2,2
    1,0,0
    1,0,0
    [p1] 승리
"""

PIN1 = 1
PIN2 = 2
BINGO = 3

MAP = [
    0,0,0,
    0,0,0,
    0,0,0
]

def printMap(arr):
    for j in range(len(arr)):
        print(arr[j], end=' ')
        if j % 3 == 2:
            print()
i = 0
while True:
    turn = PIN1
    if  i % 2 + 1 == PIN2:
        turn = PIN2
    i += 1

    # 맵출력
    printMap(MAP)

    # 인덱스 입력
    while True:
        inputIdx = int(input('[p' + str(turn) + ']인덱스 입력\n'))
        if MAP[inputIdx] != 0:
            print('이미 핀이 있는 곳입니다. 다시 입력')
        elif MAP[inputIdx] == 0:
            MAP[inputIdx] = turn
            break

    # 가로빙고체크
    count = 0
    for j in range(0, len(MAP), 3):
        count = 0
        for k in range(3):
            if MAP[j + k] == turn:
                count += 1
    if count == BINGO:
        print('[p' + str(turn) + ']승리')
        printMap(MAP)
        break
    # 세로빙고체크
    count = 0
    for j in range(3):
        count = 0
        for k in range(0, len(MAP), 3):
            if MAP[j + k] == turn:
                count += 1
    if count == BINGO:
        print('[p' + str(turn) + ']승리')
        printMap(MAP)
        break
    # 대각선빙고체크
    count = 0
    # 048 246
    if MAP[0] == turn and MAP[4] == turn and MAP[8] == turn:
        count = BINGO
    elif MAP[2] == turn and MAP[4] == turn and MAP[6] == turn:
        count = BINGO

    if count == BINGO:
        print('[p' + str(turn) + ']승리')
        printMap(MAP)
        break
    