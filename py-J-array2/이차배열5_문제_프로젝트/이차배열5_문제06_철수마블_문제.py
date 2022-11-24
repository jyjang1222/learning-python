import random
'''
	[문제]
        철수는 게임을 만들고 있다. 
        (1~6 사이의 랜덤 숫자)주사위를 던져
		해당 숫자만큼 캐릭터를 이동시킨다.
		단, 캐릭터는 외곽으로만 움직일 수 있다.
		두 바퀴를 돌고 게임을 끝내시오.
	[예시]
		옷 □ □ □ □ 
		□ ■ ■ ■ □  
		□ ■ ■ ■ □  
		□ ■ ■ ■ □  
		□ □ □ □ □  

		dice = 2   
		□ □ □ 옷 □ 
		□ ■ ■ ■ □  
		□ ■ ■ ■ □  
		□ ■ ■ ■ □  
		□ □ □ □ □  

		dice = 3   
		□ □ □ □ □  
		□ ■ ■ ■ □  
		□ ■ ■ ■ 옷 
		□ ■ ■ ■ □  
		□ □ □ □ □  

		dice = 3   
		□ □ □ □ □  
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ □ 옷 □

		dice = 1
		□ □ □ □ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ 옷 □ □

		dice = 6
		옷 □ □ □ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ □ □ □

		dice = 5
		□ □ □ □ □
		□ ■ ■ ■ 옷
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ □ □ □

		dice = 1
		□ □ □ □ □
		□ ■ ■ ■ □
		□ ■ ■ ■ 옷
		□ ■ ■ ■ □
		□ □ □ □ □

		dice = 4
		□ □ □ □ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ 옷 □ □

		dice = 4
		□ □ □ □ □
		□ ■ ■ ■ □
		옷 ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ □ □ □

		dice = 4
		□ □ 옷 □ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ □ □ □

'''

# 방법1
game = [
	['●','□','□','□','□'],
	['□','■','■','■','□'], 
	['□','■','■','■','□'], 
	['□','■','■','■','□'], 
	['□','□','□','□','□']
]


row = 0
col = 0

# 16이면 1바퀴돈후 원위치
moveAll = 0


while moveAll // 16 < 2:
	# 출력
	for i in range(len(game)):
		print(game[i])

	dice = random.randint(1, 6)
	# dice = 6
	print(dice)

	game[row][col] = '□'

	# 윗줄이고 오른줄과 안겹치면
	if row == 0 and col != len(game[0]) - 1:
		# 열에 주사위를 더했을때 우회전해야하면
		if col + dice > len(game[0]) - 1:
			# 우회전을 2번해야하면
			if dice == 6 and col == 3:
				row = len(game) - 1
				game[row][col] = '●'
				moveAll += dice
				continue
			move = col + dice - (len(game[0]) - 1)
			col = len(game[0]) - 1
			row += move
		# 열에 주사위를 더해도 회전이 필요없으면
		else:
			move = dice
			col += move
		moveAll += dice
	# 오른줄이고 아랫줄과 안겹치면
	elif col == len(game[0]) - 1 and row != len(game) - 1:
		# 행에 주사위를 더했을때 우회전해야하면
		if row + dice > len(game[0]) - 1:
			# 우회전을 2번해야하면
			if dice == 6 and row == 3:
				col = 0
				game[row][col] = '●'
				moveAll += dice
				continue
			move = row + dice - (len(game) - 1)
			row = len(game[0]) - 1
			col -= move
		# 행에 주사위를 더해도 회전이 필요없으면
		else:
			move = dice
			row += move
		moveAll += dice
	# 아랫줄이고 왼줄과 안겹치면
	elif row == len(game) - 1 and col != 0:
		# 열에 주사위를 뺐을때 우회전해야하면
		if col - dice < 0:
			# 우회전을 2번해야하면
			if dice == 6 and col == 1:
				row = 0
				game[row][col] = '●'
				moveAll += dice
				continue
			move = dice - col
			col = 0
			row -= move
		# 열에 주사위를 빼도 회전이 필요없으면
		else:
			move = dice
			col -= move
		moveAll += dice
	# 왼줄이고 윗줄과 안겹치면
	elif row != 0 and col == 0:
		# 열에 주사위를 뺐을때 우회전해야하면
		if row - dice < 0:
			# 우회전을 2번해야하면
			if dice == 6 and row == 1:
				col = len(game[0]) - 1
				game[row][col] = '●'
				moveAll += dice
				continue
			move = dice - row
			row = 0
			col += move
		# 열에 주사위를 빼도 회전이 필요없으면
		else:
			move = dice
			row -= move
		moveAll += dice
	# print(row, col)
	game[row][col] = '●'

# 출력
for i in range(len(game)):
	print(game[i])