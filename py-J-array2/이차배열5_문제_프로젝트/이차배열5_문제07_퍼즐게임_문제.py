'''
    [문제]
        철수는 게임을 만들고 있다.
        game리스트는 이차원으로 되어있다.
        game리스트 안에 block리스트의 숫자를 채워 넣는 게임이다.

        리스트의 값1은 block이 차 있는 것을 의미한다.
        리스트의 값0은 block이 비어있는 것을 의미한다.
    [조건1] 
        block은 이번에 제시된 모양이다. 
        block의 모양을 game 리스트에 넣을 수 있다면 채워 넣고,
        넣을 수 없다면 "gameover"를 출력하시오.
    [조건2]
        block을 채워 넣었을 때 가로로 1이 연속 5개이거나, 
        세로로 1이 연속 5개이면 그 줄은 전부 숫자 2로 변경하시오.
    [정답]

'''
game = [
    [0,1,0,1,0],
    [1,1,0,1,1],
    [0,1,1,1,1],
    [1,1,0,1,0],
    [0,0,0,0,0]
]

block = [
    [0,1],
    [1,1]
]

chk2 = False
# 블록은 행-1,열-1까지 비교 가능하니 길이에서 1을빼준다
for i in range(len(game) - 1):
    for j in range(len(game) - 1):
        chk = True

        # if game[i][j] == block[0][0]:
        #     if game[i][j+1] == block[0][1]:

        # 블럭1행과 게임판 비교
        for k in range(len(block)):
            # 값이 서로 달라야 채우기 가능
            if game[i][j + k] == block[0][k]:
                chk = False
        # 블럭2행과 게임판 비교
        if chk:
            for m in range(len(block)):
                # 값이 서로 달라야 채우기 가능
                if game[i + 1][j + m] == block[1][m]:
                    chk = False

        # 블럭 1,2행과 게임판과 모두 서로달라서 채울수 있므면 게임판1로 채움
        if chk:
            chk2 = True
            for n in range(len(block)):
                for o in range(len(block)):
                    if game[i+n][j+o] == 0:
                        game[i+n][j+o] = 1

# 출력
for i in range(len(game)):
    print(game[i])
print()

# 채운것이 있으면
if chk2:
    # 행에서 모두 1이면 2로 변경
    for i in range(len(game)):
        chk = True
        # 가로검사
        for j in range(len(game)):
            if game[i][j] == 0:
                chk = False
        if chk:
            for k in range(len(game[i])):
                game[i][k] = 2
        chk = True
        # 세로검사
        for j in range(len(game)):
            if game[j][i] == 0:
                chk = False
        if chk:
            for k in range(len(game[i])):
                game[k][i] = 2
    # 출력
    for i in range(len(game)):
        print(game[i])
else:
    print("gameover")

