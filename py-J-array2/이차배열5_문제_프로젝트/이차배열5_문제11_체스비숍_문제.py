import random
'''
	[문제]
		세로 가로 인덱스 두 개를 랜덤으로 저장한다. 
		그 인덱스를 기점으로 대각선 방향으로 전부 1로 채운 후 출력하시오.
		    
		[예]
			y = 2
			x = 1
		    	
			[0,0,0,1,0]
			[1,0,1,0,0]
			[0,1,0,0,0]
			[1,0,1,0,0]
			[0,0,0,1,0]
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

for i in range(len(list)):
	print(list[i])
		
