import random

"""
    [문제]
        랜덤숫자(1~10)사이의 숫자중 짝수만 5개 출력하시오.

"""
# print("--[문제1]--")


'''
    [문제]
        무한반복문을 활용해서 
        눈금이 1~6 인 주사위 두개를 던진다.
        주사위1 과 주사위2 의 차이가 1일때 가 연속으로 두번나오면 게임은 종료된다.
        주사위의 눈금을 전부 출력하시오. 
    [예시]
        1, 4 (카운트0)
        2, 4 (카운트0)
        4, 3 (카운트1)
        6, 1 (카운트0)
        2, 3 (카운트1)
        4, 5 (카운트2) 종료
       
'''
# print("--[문제2]--")


"""
    [문제]
        철수는 학원에 갈때는 걸어서 시속 4키로미터로 가고 
        올때는 자전거를 타고 시속 6키로미터로 왔다.
        가는데 오는데 시간을 합쳐서 5시간이 걸렸다고했을때
        집과 학원의 거리는 얼마인지구하시오. 
        가느데 걸린시간과 오는데 걸린시간도 구하시오.
        주석으로 풀이 하시오.
"""
# print("--[문제3]--")


# 1
count = 0
while True:
    r = random.randint(1, 10)
    if r % 2 == 0:
        print(r, end = " ")
        count += 1
    if count == 5:
        break


print()
# 2
# 1차 풀이
# while True:
#     count = 0
#     for i in range(2):
#         dice1 = random.randint(1, 6)
#         dice2 = random.randint(1, 6)
#         print(dice1, dice2, count)
#         if dice2 - dice1 == 1 or dice1 - dice2 == 1:
#             count += 1
#             print(dice1, dice2, count)
#         if count == 2:
#             break
#     if count == 2:
#         break

# 2차 풀이
count = 0
while True:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice2 - dice1 == 1 or dice1 - dice2 == 1:
        count += 1
    print(dice1, dice2, count)
    if count == 1:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        if dice2 - dice1 == 1 or dice1 - dice2 == 1:
            count += 1
        else:
            count = 0
        print(dice1, dice2, count)
    if count == 2:
        break

# 3
'''
거리 = 속력 * 시간
시간 = 거리 / 속력

5 = 거리 / 4 + 거리 / 6
5 * 12 = 거리 * 3 + 거리 * 2
60 = 거리 * 5
거리 = 12km

가는시간 = 12 / 4 = 3h
오는시간 = 12 / 6 = 2h

'''
# time = 5
# walkSpd = 4
# bikeSpd = 6


