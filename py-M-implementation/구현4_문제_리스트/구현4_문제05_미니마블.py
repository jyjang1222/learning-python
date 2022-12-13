import random
"""
 	[미니마블]
	 
		1. 플레이어는 [p1]과 [p2] 2명이다. 한번씩 번갈아 가면서 행동한다. 
		2. [1.주사위][2.패스] 를 선택할수있다. 주사위는 (1~4)의 랜덤값을 가진다. 
		3. 주사위숫자만큼 현재위치에서 앞으로 이동한다. 
		4. 이동한자리가 다른 플레이어와 같은 위치에 놓이게 되면, 상대 플레이어는 잡히게 되어 맨앞(인덱스 0) 으로 강제 이동된다.
		5. 상대를 잡은 위치가 맨앞(인덱스 0)의 위치에 있을때는 안전지대이다.(잡히지않는다.)
		6. 이동거리가 배열의 마지막위치를 초과하면, 맨앞(인덱스 0)으로 이동하고 초과한숫자만큼 추가이동한다.
		7. 먼저 3바퀴를 돌면 이긴다.
		
		[예시]   
		   [p1] 주사위 : 1
		   1 0 0 0 0 0 0 0 0 0
		   2 0 0 0 0 0 0 0 0 0
		   
		   [p2] 주사위 : 3
		   0 1 0 0 0 0 0 0 0 0
		   0 0 0 2 0 0 0 0 0 0
		   
		   [p1] 주사위 : 2  , [p1]이 [p2]를 잡았다!	   
		   0 0 0 1 0 0 0 0 0 0
		   2 0 0 0 0 0 0 0 0 0 
"""

p1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
p2 = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def showMap():
	print(p1)
	print(p2)

def changeTurn(currentTurn):
	if currentTurn == P1TURN:
		currentTurn = P2TURN
	elif currentTurn == P2TURN:
		currentTurn = P1TURN
	return currentTurn

P1TURN = 1
P2TURN = 2
turn = P1TURN
p1count = 0
p2count = 0
p1idx = 0
p2idx = 0
while True:
	DICE = 1
	PASS = 2
	showMap()
	message = '[1.주사위][2.패스] turn: p' + str(turn) + ', ' + 'p1count: ' + str(p1count) + ', ' + 'p2count: ' + str(p2count) + '\n'
	select = int(input(message))
	if select == DICE:
		r = random.randint(1, 4)
		print('dice:', r)
		if turn == P1TURN:
			p1[p1idx] = 0
			if p1idx + r >= len(p1):
				p1idx = p1idx + r - len(p1)
				p1count += 1
			else:
				p1idx += r
			# 같은 위치라면
			if p1idx == p2idx and p2idx != 0:
				p2[p2idx] = 0
				p2idx = 0
				p2[p2idx] = 2
			p1[p1idx] = 1
		elif turn == P2TURN:
			p2[p2idx] = 0
			if p2idx + r >= len(p2):
				p2idx = p2idx + r - len(p2)
				p2count += 1
			else:
				p2idx += r
			# 같은 위치라면
			if p2idx == p1idx and p1idx != 0:
				p1[p1idx] = 0
				p1idx = 0
				p1[p1idx] = 1
			p2[p2idx] = 2
		
		turn = changeTurn(turn)
	elif select == PASS:
		turn = changeTurn(turn)
		continue
	if p1count >= 3 or p2count >= 3:
		showMap()
		print('p1count:', p1count, 'p2count:',  p2count)
		break