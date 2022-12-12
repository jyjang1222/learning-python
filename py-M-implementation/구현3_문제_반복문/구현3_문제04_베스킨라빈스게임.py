"""	
	[베스킨라빈스31]
		베스킨라빈스 게임이란, 플레이어 2명이 번갈아가면서
		1~3사이의 숫자를 선택할수있고, 그 숫자들을 계속 더해서 
		그 누적합이 31에 먼저도달한쪽이 지는게임이다.
	 
	[조건]
		1) 각 플레이어는 번갈아가면서 1~3을 선택한다.
		2) 만약에 이상한숫자를 입력하면 1~3을 입력할때까지 계속본인 차례이다.
		3) 각 플레이어가 선택한숫자는  total  변수에 계속 누적해서 더한다.
		4) total 이 31이상에 도달하면 승리자를 출력한다.
"""

total = {'player1' : 0, 'player2' : 0}

while True:
	while True:
		player1 = int(input('player1 숫자입력'))
		if player1 == 1 or player1 == 2 or player1 == 3:
			break
	while True:
		player2 = int(input('player2 숫자입력'))
		if player2 == 1 or player2 == 2 or player2 == 3:
			break

	total['player1'] += player1
	total['player2'] += player2

	if total['player1'] >= 31 and total['player2'] >= 31:
		print('무승부', total['player1'], total['player2'])
		break
	if total['player1'] >= 31:
		print('player1 승리', total['player1'], total['player2'])
		break
	if total['player2'] >= 31:
		print('player2 승리', total['player1'], total['player2'])
		break