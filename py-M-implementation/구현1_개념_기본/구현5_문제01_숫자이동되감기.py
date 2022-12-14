"""
	[숫자이동되감기]
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
		# 값교체
		tmp = a[posY][posX-1]
		a[posY][posX-1] = 0
		a[posY][posX] = tmp
		# 로그저장
		dict['y'] = posY
		dict['x'] = posX-1
		posData.append(dict)
		# 현재인덱스이동
		posX -= 1
	elif inputNumber == 2:
		if posX+1 >= len(a[posY]):
			print('끝이라서 이동할수 없습니다.')
			continue
		tmp = a[posY][posX+1]
		a[posY][posX+1] = 0
		a[posY][posX] = tmp
		dict['y'] = posY
		dict['x'] = posX+1
		posData.append(dict)
		posX += 1
	elif inputNumber == 3:
		if posY-1 < 0:
			print('끝이라서 이동할수 없습니다.')
			continue
		tmp = a[posY-1][posX]
		a[posY-1][posX] = 0
		a[posY][posX] = tmp
		dict['y'] = posY-1
		dict['x'] = posX
		posData.append(dict)
		posY -= 1
	elif inputNumber == 4:
		if posY+1 >= len(a):
			print('끝이라서 이동할수 없습니다.')
			continue
		tmp = a[posY+1][posX]
		a[posY+1][posX] = 0
		a[posY][posX] = tmp
		dict['y'] = posY+1
		dict['x'] = posX
		posData.append(dict)
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