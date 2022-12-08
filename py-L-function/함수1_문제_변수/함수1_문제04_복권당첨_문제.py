'''
    [문제]
        lotto리스트가 당첨인지 꽝인지 체크하는 함수를 만드시오.
        단, 7이 연속으로 3개이면 당첨이다.
    [정답]
        당첨
'''

lotto = [1, 7, 7, 1, 7, 7, 7]

def lottery(arr):
    cnt = 0
    for i in arr:
        if i == 7:
            cnt += 1
        else:
            cnt = 0
    if cnt == 3:
        print('당첨')
    else:
        print('꽝')

lottery(lotto)