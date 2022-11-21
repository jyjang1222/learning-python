import random
"""
[문제]
    아래 리스트에 랜덤숫자 (1~30) 을  10개 저장한다. 
    단, 홀수만 저장하고 , 중복숫자는 없어야 한다. 
[예시]
    a = [29, 1, 5, 9 , 21, 25, 7, 3, 13, 15]

"""

a = []

while True:
    if len(a) == 10:
        break

    chk = True
    r = random.randint(1, 30)

    if r % 2 == 0:
        continue

    for i in range(len(a)):
        if a[i] == r:
            chk = False
    if chk:
        a.append(r)

print(a)

# 1차반복문만 사용
a = []
i = 0
chk = True
while True:
    r = random.randint(1, 30)
    if r % 2 == 1:
        a.append(r)
        break

while True:
    if len(a) == 10:
        break

    # 홀수짝수체크
    if r % 2 == 0:
        r = random.randint(1, 30)
        continue
    
    if i == len(a) and len(a) > 1:
        i = 0
        chk = True
        r = random.randint(1, 30)
    if len(a) == 1 and a[0] == r:
        r = random.randint(1, 30)
        continue
    
    # 중복숫자가 있으면 chk = False
    if len(a) > 1 and a[i] == r:
        chk = False
    # 중복숫자가 없으면 chk = true
    if i == len(a) - 1 and chk == True:
        a.append(r)
        chk = False

    i += 1

print(a)

# 학생풀이
import random

a = []
oddList = []

# 1부터 30까지 홀수 리스트를 먼저 뽑아놓음
for i in range(30):
    i += 1
    if i % 2 != 0:
        oddList.append(i)

#홀수리스트에서 랜덤으로 가져다가 a 리스트에 추가함
for i in range(10):
    idx = random.randint(0, len(oddList) - 1)
    a.append(oddList[idx])
    del oddList[idx]

print(a)

