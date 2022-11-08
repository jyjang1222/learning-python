import random
'''
    [문제]
        철수는 게임을 하고 있다. 
        monster는 게임의 적 4마리를 의미하고 9는 몬스터의 체력을 의미한다.
        철수의 공격력은 5이다.     
        랜덤으로 몬스터 중 하나를 선택해서 공격하고,
        이를 총 다섯 번 반복한다. 
        모든 몬스터를 공격한 후 몬스터들의 체력을 출력하시오.
        단, 몬스터 체력은 0이 되면 더 이상 내려가지 않는다. 
        또한 공격한 몬스터의 양쪽에게는 1의 대미지를 가하게 된다. 체력이 0인 몬스터는 공격할 수 없고 다른 몬스터를 선택해야 한다.
        
'''

monster = [9,7,8,6]
power = 5
count = 0

while count < 5:
    r = random.randint(0, len(monster) - 1)

    if monster[r] == 0:
        print("다시공격")
        continue
    elif monster[r] != 0:
        monster[r] -= power
        if monster[r] < 0:
            monster[r] = 0
        count += 1
        # 왼쪽끝 공격
        if r == 0:
            monster[r + 1] -= 1
            if monster[r + 1] < 0:
                monster[r + 1] = 0
        # 오른쪽끝 공격
        elif r == len(monster) - 1:
            monster[r - 1] -= 1
            if monster[r - 1] < 0:
                monster[r - 1] = 0
        # 가운데 공격
        else:
            monster[r + 1] -= 1
            if monster[r + 1] < 0:
                monster[r + 1] = 0
            monster[r - 1] -= 1
            if monster[r - 1] < 0:
                monster[r - 1] = 0
    
    print(r, "몬스터공격!", monster)
