import random
'''
	[문제]
		철수는 철수의 마블 게임을 개발 중이다. 
		map1과 map2는 게임 스테이지를 표현한다. 
		숫자 1은 철수의 위치이다. 
		주사위는 1~6까지 있고 주사위 2개를 던저서 그 합만큼 앞으로 이동한다. 		
		map1의 끝에 도달하면 map2로 이동해서 전진하고, 
		map2의 끝에 도달하면 다시 map1로 이동해서 전진한다. 		
		주사위를 총 4번 반복하고 철수의 위치를 출력하시오.
	[예시]
	(1)	시작
		map1 = [1,0,0,0,0,0,0,0,0,0]
		map2 = [0,0,0,0,0,0,0,0,0,0]
  
	(2)	주사위 3 , 5 : 8
		map1 = [0,0,0,0,0,0,0,0,1,0]
		map2 = [0,0,0,0,0,0,0,0,0,0]
		
	(3)	주사위 2 , 1 : 3
		map1 = [0,0,0,0,0,0,0,0,0,0]
		map2 = [0,1,0,0,0,0,0,0,0,0]
		
	(4)	주사위 6 , 1 : 7
		map1 = [0,0,0,0,0,0,0,0,0,0]
		map2 = [0,0,0,0,0,0,0,0,1,0]
		
	(5)	주사위 3 , 3 : 6
		map1 = [0,0,0,0,1,0,0,0,0,0]
		map2 = [0,0,0,0,0,0,0,0,0,0]
			
'''

map1 = [1,0,0,0,0,0,0,0,0,0]
map2 = [0,0,0,0,0,0,0,0,0,0]

idx = 0
map = 1

print("map1  ", map1)
print("map2  ", map2)

for i in range(4):
	r1 = random.randint(1, 6)
	r2 = random.randint(1, 6)

	sum = r1 + r2
	
	
	# 현재위치가 map1일때
	if map == 1:
		map1[idx] = 0
		# 주사위합이 map1 남은길이 보다 같거나크면 map2로 이동
		if (len(map1) - 1) - idx <= sum:
			# 이동거리(주사위합) - map1남은길이 -> 맵전환후 이동거리
			idx = sum - (len(map1) - 1 - idx) - 1
			map2[idx] = 1
			map = 2
		else:
			idx = sum % len(map1)
			map1[idx] = 1
	# 현재위치가 map2일때
	elif map == 2:
		map2[idx] = 0
		# 주사위합이 map2 남은길이 보다 같거나크면 map1로 이동
		# idx는 0 부터시작이라서 1을 빼줘야한다..
		if (len(map2) - 1) - idx <= sum:
			idx = sum - (len(map2) - 1 - idx) - 1
			map1[idx] = 1
			map = 1
		else:
			idx = sum % len(map2)
			map2[idx] = 1

	print(sum, "map1", map1)
	print(sum, "map2", map2)
	# sum % len(map1) 이동
