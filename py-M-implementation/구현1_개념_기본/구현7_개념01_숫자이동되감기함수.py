"""
	[숫자이동되감기] 함수로 구현하시오.
		[그림]
			[1,2,3],
			[4,5,6],
			[7,8,9]   
  
		[메뉴]  1) left 2)right 3)up 4)down 5)replay  		 
			0 이 플레이어이다 .
			번호를 입력받고 해당위치로 이동
			이동할때 값을 서로 교환한다. 

			[예시] left ==> 8과 0 이 위치를 바꾼다.
				[1,2,3],
				[4,5,6],
				[7,0,8]
	
			[예시] left ==> 7과 0 이 위치를 바꾼다.
				[1,2,3],
				[4,5,6],
				[0,7,8]	

			[예시] replay ==> 전위치로 되돌아간다.
				[1,2,3],
				[4,5,6],
				[7,0,8]	
"""

a = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]


while True:
	inputNumber = int(input('1 ~ 9 사이의 수를 입력해주세요.\n'))
	if 1 <= inputNumber and inputNumber <= 9:
		break
	else:
		print('다시 입력해주세요.')

posData = []
posY = 0
posX = 0

for i in range(len(a)):
	for j in range(len(a[i])):
		if a[i][j] == inputNumber:
			a[i][j] = 0
			dict = {}

			dict['y'] = i
			dict['x'] = j
			posY = i
			posX = j
			posData.append(dict)
		
for i in a:
	print(i)

# 1) left 2)right 3)up 4)down 5)replay
# def left(y, x):
# 	# 값교체
# 	dict = {}
# 	tmp = a[y][x-1]
# 	a[y][x-1] = 0
# 	a[y][x] = tmp
# 	# 로그저장
# 	dict['y'] = y
# 	dict['x'] = x-1
# 	posData.append(dict)

# def right(y, x):
# 	tmp = a[y][x+1]
# 	a[y][x+1] = 0
# 	a[y][x] = tmp
# 	dict['y'] = y
# 	dict['x'] = x+1
# 	posData.append(dict)

# def up(y, x):
# 	tmp = a[y-1][x]
# 	a[y-1][x] = 0
# 	a[y][x] = tmp
# 	dict['y'] = y-1
# 	dict['x'] = x
# 	posData.append(dict)

# def down(y, x):
# 	tmp = a[y+1][x]
# 	a[y+1][x] = 0
# 	a[y][x] = tmp
# 	dict['y'] = y+1
# 	dict['x'] = x
# 	posData.append(dict)

LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'

def move(y, x, direction):
	dict = {}
	tmp = a[y][x-1]
	if direction == LEFT or direction == RIGHT:
		dict['y'] = y
		if direction == LEFT:
			tmp = a[y][x-1]
			a[y][x-1] = 0
			a[y][x] = tmp
			# 로그저장
			dict['x'] = x-1
		if direction == RIGHT:
			tmp = a[y][x+1]
			a[y][x+1] = 0
			a[y][x] = tmp
			dict['x'] = x+1
	elif direction == DOWN or direction == UP:
		dict['x'] = x
		if direction == UP:
			tmp = a[y-1][x]
			a[y-1][x] = 0
			a[y][x] = tmp
			dict['y'] = y-1
		if direction == DOWN:
			tmp = a[y+1][x]
			a[y+1][x] = 0
			a[y][x] = tmp
			dict['y'] = y+1
	posData.append(dict)

while True:
	inputNumber = int(input('1) left 2)right 3)up 4)down 5)prev 6) esc\n'))
	if not(1 <= inputNumber and inputNumber <= 6):
		print('1 ~ 6 사이의 수를 입력해주세요.')
		continue

	dict = {}
	tmp = 0
	if inputNumber == 1:
		if posX-1 < 0:
			print('끝이라서 이동할수 없습니다.')
			continue
		move(posY, posX, LEFT)
		# 현재인덱스이동
		posX -= 1
	elif inputNumber == 2:
		if posX+1 >= len(a[posY]):
			print('끝이라서 이동할수 없습니다.')
			continue
		move(posY, posX, RIGHT)
		posX += 1
	elif inputNumber == 3:
		if posY-1 < 0:
			print('끝이라서 이동할수 없습니다.')
			continue
		move(posY, posX, UP)
		posY -= 1
	elif inputNumber == 4:
		if posY+1 >= len(a):
			print('끝이라서 이동할수 없습니다.')
			continue
		move(posY, posX, DOWN)
		posY += 1
	elif inputNumber == 5:
		if len(posData) == 1:
			print('더이상 뒤로가기 할수 없습니다.')
			continue
		del posData[-1]
		tmp = a[posData[-1]['y']][posData[-1]['x']]
		a[posData[-1]['y']][posData[-1]['x']] = 0
		a[posY][posX] = tmp
		posY = posData[-1]['y']
		posX = posData[-1]['x']
	else:
		break
	
	for i in a:
		print(i)
	# print(posData)