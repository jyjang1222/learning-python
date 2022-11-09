import random
'''
	[문제]
		철수는 마블 게임을 하고 있다.
		map리스트는 철수가 움직일 수 있는 공간을 리스트로 표현한 것이다.
		숫자 1은 철수의 현재 위치를 의미한다.

		주사위(1~6)를 던져서 랜덤숫자만큼 1을 전진시킨다. 	
		만약 1이 끝까지 도달하면 다시 맨 앞으로 이동해서 전진한다.
		총 4회 반복하면서 철수의 위치를 출력하시오.
	[예시]
		(1) 시작
			map = [1,0,0,0,0,0,0,0,0,0]
  		(2) 주사위 : 5
			map = [0,0,0,0,0,1,0,0,0,0]
		(3) 주사위 : 3
			map = [0,0,0,0,0,0,0,0,1,0]
		(4) 주사위 : 6
			map = [0,0,0,0,1,0,0,0,0,0]
		(5) 주사위 : 4
			map = [0,0,0,0,0,0,0,0,1,0]
'''

map = [1,0,0,0,0,0,0,0,0,0]
print(map)

idx = 0
for i in range(len(map)):
	if map[i] == 1:
		idx = i
# print(idx)	

for i in range(4):
	r = random.randint(1, 6)
	# 현재위치 idx를 찾는 반복문
	for j in range(len(map)):
		if map[j] == 1:
			idx = j
			map[j] = 0
	# 현재위치 idx에 주사위눈+
	idx += r
	# idx가 map길이를 넘어서면 처음으로
	if idx > len(map) - 1:
		idx -= len(map)
	map[idx] = 1
	print(r, map, idx)


# position = 0

# for i in range(4):
# 	move = random.randint(1, 6)

# 	map[position] = 0

# 	position += move
# 	position %= len(map)

# 	map[position] = 1

# 	print(move, map)
