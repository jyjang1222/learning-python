'''
	[문제]
		철수는 산전수전 끝에 50층 빌딩의 건물주가 되었다. 
		철수는 빌딩의 엘리베이터에서 숫자 4를 전부 제거 했다. 
		만약에 실제로 4층을 간다면 숫자 5를 눌러야 한다. 
		철수의 빌딩은 지상 1층에서 지상 50층이고, 
		실제 층과 엘리베이터에 적혀있는 숫자를 1층부터 순서대로 출력하시오. 
  
	[결과]
		1 1
		2 2
		3 3
		4 5
		5 6
		6 7
		7 8
		8 9
		9 10
		10 11
		11 12
		12 13
		13 15
		14 16
		15 17
		16 18
		17 19
		18 20
		19 21
		20 22
		21 23
		22 25
		23 26
		24 27
		25 28
		26 29
		27 30
		28 31
		29 32
		30 33
		31 35
		32 36
		33 37
		34 38
		35 39
		36 50
		37 51
		38 52
		39 53
		40 55
		41 56
		42 57
		43 58
		44 59
		45 60
		46 61
		47 62
		48 63
		49 65
		50 66
'''

# i = 1
# floor = 1
# count = 0

# while i <= 50:
# 	if i // 10 == 4:
# 		if floor % 10 == 4:
# 			floor += 1
# 		print(i, floor)
# 		floor += 1
# 		i += 1
# 		continue
# 	if i % 10 == 4 :
# 		floor += 1
# 	if floor == 40:
# 		floor += 10
# 	print(i, floor)

# 	floor += 1
# 	i += 1

# 2트
# fakeFloor = 1
# for realFloor in range(1, 51):
# 	n = fakeFloor
# 	chk = False
# 	while n != 0:
# 		if n % 10 == 4:
# 			chk = True
# 		n //= 10
# 	if chk:
# 		fakeFloor += 1
# 	print(realFloor, fakeFloor)
# 	if fakeFloor == 39:
# 		fakeFloor += 9
# 	fakeFloor += 1


# 3트
# fakeFloor = 1
# realFloor = 1

# while realFloor <= 50:
# 	if fakeFloor % 10 == 4:
# 		fakeFloor += 1
# 	if fakeFloor // 10 == 4:
# 		fakeFloor += 10
# 	print(realFloor, fakeFloor)
# 	fakeFloor += 1
# 	realFloor += 1

# 4트
realFloor = 1
elevator = 1

while realFloor <= 500:
	n = elevator
	total = 0
	count = 1
	# 464 43 4
	while n != 0:
		if n % 10 == 4:
			total += count
		count *= 10
		n //= 10

	elevator += total

	print(realFloor, elevator)
	elevator += 1
	realFloor += 1