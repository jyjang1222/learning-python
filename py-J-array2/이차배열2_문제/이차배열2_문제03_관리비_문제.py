import random
'''
    apt 리스트는 아파트 1동의 각 세대를 의미한다.
    pay 는 이번달 관리비를 뜻한다.
'''

apt = [
		[101, 102, 103],	
		[201, 202, 203],	
		[301, 302, 303]		
	]		
pay = [
		[1000, 2100, 1300],	 
		[4100, 2000, 1000],	 
		[3000, 1600,  800]  
	]
rank = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

'''
    [문제 1] 
        각 층별 관리비 합을 출력하시오.
    [정답 1] 
        4400 7100 5400
'''

print("[문제1]")
for i in range(len(pay)):
    sum = 0
    for j in range(len(pay[i])):
        sum += pay[i][j]
    print(sum, end = " ")
print()


'''
    [문제 2] 
        랜덤으로 호수와 관리비 한개 출력하시오.
    [예시 2]
        0 2
        103 1300 원 
'''

print("[문제2]")
r1 = random.randint(0, len(apt) - 1)
r2 = random.randint(0, len(apt[0]) - 1)

print(r1, r2, pay[r1][r2])

'''
    [문제 3] 
        관리비가 가장 많이 나온 집, 가장 적게 나온 집을 출력하시오.
    [정답 3]
        가장 많이 나온 집 = 201
        가장 적게 나온 집 = 303    
'''
print("[문제3]")
max = 0
min = 5000

for i in range(len(pay)):
    for j in range(len(pay[i])):
        if pay[i][j] > max:
            max = pay[i][j]
            maxIdx1 = i
            maxIdx2 = j
        if pay[i][j] < min:
            min = pay[i][j]
            minIdx1 = i
            minIdx2 = j

print(apt[maxIdx1][maxIdx2], apt[minIdx1][minIdx2])

'''     
    [문제 4] 
        관리비 많이나온 순서대로 rank리스트에 등수를 저장하시오.
    [정답 4]
        [7, 3, 6]
        [1, 4, 7]
        [2, 5, 9]
'''
print("[문제4]")

pay2 = []
for i in range(len(pay)):
    for j in range(len(pay[i])):
        pay2.append(pay[i][j])

pay2 = [1000, 2100, 1300, 4100, 1000, 1000, 3000, 1600, 800]
print(pay2)

rank2 = []
for i in range(len(rank)):
    for j in range(len(rank[i])):
        rank2.append(0)
# print(rank2)

prev = 5000
i = 1
while i < 10:
    # max 찾기
    max = 0
    for j in range(len(pay2)):
        if pay2[j] > max and pay2[j] < prev:
            max = pay2[j]
            maxIdx = j
    # 같은순위체크
    cnt = 0
    for j in range(len(pay2)):
        if max == pay2[j]:
            cnt += 1
    prev = max
    rank2[maxIdx] = i
    # 같은순위수만큼 i += 1
    if cnt >= 2:
        for m in range(len(pay2)):
            if max == pay2[m]:
                rank2[m] = i
        for m in range(cnt - 1):
            i += 1
    print(rank2)
    i += 1
# print(rank2)

n = 0
for i in range(len(rank)):
    for j in range(len(rank[i])):
        rank[i][j] = rank2[n]
        n += 1
print(rank)


# 다음에 풀어볼 방법
rank3 = []
for i in range(len(pay2)):
    count = 1
    for j in range(len(pay2)):
        if pay2[i] < pay2[j]:
            count += 1
    rank3.append(count)
print(rank3)
# 순위 = 1 + 자기자신보다 큰수의 갯수

