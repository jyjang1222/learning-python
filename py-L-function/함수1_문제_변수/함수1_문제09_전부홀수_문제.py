import random
'''
    [문제]
        리스트에 랜덤으로 -100 ~ 100 사이의 홀수 4개를 저장 후,
        전부 홀수인지 검사하는 함수를 만드시오.
    [예시]
        [-5, 99, -71, 27] 전부 홀수이다.
        [0, 22, -41, 21] 전부 홀수가 아니다.
'''

def isAllOdd(arr):
    chk = True
    for i in arr:
        if i % 2 == 0 and i != 0:
            chk = False
    print(arr)
    print(chk)

randomArr = []

while True:
    r = random.randint(-100, 100)
    if r % 2 == 1:
        randomArr.append(r)
    if len(randomArr) == 4:
        break

isAllOdd(randomArr)
