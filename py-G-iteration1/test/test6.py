import random
# 1

a = 0
b = 0
winA = 0
winB = 0
sum1 = 0
sum2 = 0

while True:
    if winA == 3 or winB == 3:
        break

    r1 = random.randint(1, 6)
    r2 = random.randint(1, 6)
    r3 = random.randint(1, 6)
    r4 = random.randint(1, 6)
    # print(r1,r2,r3,r4)
    sel1 = random.randint(0, 1)
    sel2 = random.randint(0, 1)

    # 주사위 선택
    sum1 = r1 + r2
    sum2 = r3 + r4
    # print(sum1, sum2)
    # print(sel1,sel2)

    if sel1 == 0:
        a = sum1
    elif sel1 == 1:
        a = sum2

    if sel2 == 0:
        b = sum1
    elif sel2 == 1:
        b = sum2

    # print(a, b)

    # 승부가르기
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            print(a, b, "a가 이김")
            if winB != 0:
                winA = 0
                # winB = 0
            winA += 1
        elif a < b:
            print(a, b, "b가 이김")
            if winA != 0:
                # winA = 0
                winB = 0
            winB += 1
        else:
            print(a, b, "무승부")
            winA = 0
            winB = 0
    elif a % 2 == 1 and b % 2 == 1:
        if a < b:
            print(a, b, "b가 이김")
            if winA != 0:
                # winA = 0
                winB = 0
            winB += 1
        elif a > b:
            print(a, b, "a가 이김")
            if winB != 0:
                winA = 0
                # winB = 0
            winA += 1
        else:
            print(a, b, "무승부")
            winA = 0
            winB = 0   
    else:
        print(a, b, "무승부")
        winA = 0
        winB = 0
    print(winA, winB)

