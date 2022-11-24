import random
'''
	[문제]
		세로 가로 인덱스 두개를 랜덤으로 저장한다. 
		그 인덱스를 기점으로 대각선 + 십자가 방향으로 전부 1로 채운후 출력하시오.
		
		[예]
			y = 3 , x = 0
			
			[1, 0, 0, 1, 0]
			[1, 0, 1, 0, 0]
			[1, 1, 0, 0, 0]
			[1, 1, 1, 1, 1]
			[1, 1, 0, 0, 0]
'''
list = [
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0]
]

y = random.randint(0, 4)
x = random.randint(0, 4)
print("y:",y,"x:",x)
list[y][x] = 1

for i in range(len(list)):
	for j in range(len(list)):
		# 1시방향
		for k in range(len(list)):
			if y-k < 0 or x+k >= len(list):
				continue
			list[y-k][x+k] = 1
		# 5시방향
		for k in range(len(list)):
			if y+k >= len(list) or x+k >= len(list):
				continue
			list[y+k][x+k] = 1
		# 7시방향
		for k in range(len(list)):
			if y+k >= len(list) or x-k < 0:
				continue
			list[y+k][x-k] = 1
		# 11시방향
		for k in range(len(list)):
			if y-k < 0 or x-k < 0:
				continue
			list[y-k][x-k] = 1
		# 12시방향
		for k in range(len(list)):
			if y-k < 0:
				continue
			list[y-k][x] = 1
		# 가로
		for k in range(len(list)):
			list[y][k] = 1
		# 6시방향
		for k in range(len(list)):
			if y+k >= len(list):
				continue
			list[y+k][x] = 1

for i in range(len(list)):
	print(list[i])










	