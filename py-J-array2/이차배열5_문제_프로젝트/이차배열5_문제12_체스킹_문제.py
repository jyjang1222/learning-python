import random
'''
	[문제]
		세로 가로 인덱스 두개를 랜덤으로 저장한다. 
		그 인덱스를 기점으로 십자가 방향으로 전부 1로 채운후 출력하시오.
		
		[예]
			y = 1 , x = 4
			[0, 0, 0, 0, 1]
			[1, 1, 1, 1, 1]
			[0, 0, 0, 0, 1]
			[0, 0, 0, 0, 1]
			[0, 0, 0, 0, 1]
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

for k in range(len(list)):
	# 가로
	list[y][k] = 1
	# 세로
	list[k][x] = 1

for i in range(len(list)):
	print(list[i])

