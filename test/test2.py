import random

"""
[문제]
	철수는 농구공을 18번던저 11번 성공했다.
	철수의 성공 확률을 출력하시오.
    소수점 2자리로 구하시오.
"""

# 1
print("#1")
shoot = 18
success = 11
percent = round(success / shoot, 2)
print(percent)
print(percent * 100, "%")

print()

"""
[문제]
	철수는 12초에 100미터를 달린다.
	철수의 시속을 구하시오. 
	단, 철수는 일정한속도로 달린다.
    소수점 2자리로 구하시오.
"""

# 2
print("#2")
'''
거리 = 속력 * 시간
속력 = 거리 / 시간
'''

거리 = 100
시간 = 12
속력 = round(거리 / 시간, 2)
print(속력,"m/s")
print(속력 * 60, "m/m")
print(속력 * 60 * 60, "m/h")

print()

"""
[문제]
    1부터 100사이의 랜덤숫자를 변수a에 저장한다. 
    a의 값이 1~5사이면 b에 95 저장후 출력
    a의 값이 6~10사이면 b에 90 을저장후 출력 
    a의 값이 11~15사이면 b에 85 를저장후 출력
    ....
    ....
    a의 값이 91~95 사이면 b에 5를 저장후 출력
    a의 값이 96~100 사이면 b에 0을 저장후 출력 
"""

# 3
print("#3")
a = random.randint(1, 100)
print("a:", a)
j = 95
for i in range(1, 101, 5):
    if i <= a and a < i + 5: 
        print(j)
    j -= 5

print()

"""
[문제]	
	자동차 카센터에는 수리를 기다리는 오토바이와 자동차가 있다.
	오토바이와 자동차를 합쳐서 21대가 있다.
	바퀴는 합쳐서 70개 일때 오토바이와 자동차의 대수를 구하시오.
"""

# 4
print("#4")
자동차 = 0
오토바이 = 21


while True:
    자동차 += 1
    오토바이 -= 1

    if 자동차 * 4 + 오토바이 * 2 == 70:
        print("자동차:", 자동차, "오토바이:", 오토바이)
        break

print()

"""
[문제] 
    1000보다 큰 수중에서 12의 배수를 검색하고, 
    십의자리가 4인 수를
    가장 작은 수부터 차례대로 4개를 출력하시오. 
"""

print("#5")

i = 1001
cnt = 0
while True:
    if i % 12 == 0:
        if i % 100 // 10 == 4:
            print(i, end = " ")
            cnt += 1
    if cnt == 4:
        break
    i += 1

print()

"""
[문제]
    100 ~ 999 사이의 숫자를 랜덤으로 3개 출력한다. 
    단, 전부 각각의숫자마다 숫자5가 한개이상 포함되어야한다.
[예시]
    145
    536
    955
"""

print("#6")
# 방법1
cnt = 0

while True:
    r1 = random.randint(1,9)
    r2 = random.randint(0,9)
    r3 = random.randint(0,9)

    if r1 == 5 or r2 == 5 or r3 == 5:
        print(r1, end = "")
        print(r2, end = "")
        print(r3, end = "")
        cnt += 1
        print()
    if cnt == 3:
        break
# 방법2
cnt = 0

while True:
    r = random.randint(100, 999)

    if r // 100 == 5 or r % 100 // 10 == 5 or r % 10 == 5:
        print(r, end = "")
        cnt += 1
        print()
    if cnt == 3:
        break

print()

"""
[문제]
    a = [] 
    a리스트에 1~5사이의 랜덤숫자 15개를 저장한다.
    숫자 1 2 3 이 연속으로 나오면 당첨이라고 할때,
    당첨이 몇번나왔는지 출력하시오.
[예시]

    a = [1, 5, 2, 1, 2, 3, 3, 2, 1, 4, 1, 2, 3, 4, 2] 
    당첨: 2번
"""

print("#7")
a = []
for i in range(15):
    r = random.randint(1, 5)
    a.append(r)

# a = [1, 5, 2, 1, 2, 3, 3, 2, 1, 4, 1, 2, 3, 4, 2] 
# a = [1, 5, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 2] 
# 길이 - 2 까지 비교가능
cnt = 0
for i in range(len(a) - 2):
    chk = True
    for j in range(3):
        # 1 ~ 3이 아니면 false
        # a[i + j] < 1 or 3 < a[i + j]
        if not(1 <= a[i + j] and a[i + j] <= 3):
            chk = False
    if chk:
        cnt += 1

print(a, cnt)