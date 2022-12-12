import random
"""
[문제]
	[가위 바위 보 게임]
		1. player1 은 가위 바위 보중 하나를 입력받는다. 
		2. com 은 랜덤으로 가위 바위 보를 고른다. 
		3. 결과를 출력한다.
"""
SCISSORS = '가위'
ROCK = '바위'
PAPER = '보'

while True:
	player = input('가위, 바위, 보를 입력하세요.\n')
	if player == SCISSORS or player == ROCK or player == PAPER:
		break

com = random.randint(0, 2)
if com == 0:
	com = SCISSORS
if com == 1:
	com = ROCK
if com == 2:
	com = PAPER

res = ''

if player == com:
	res = '무승부'
elif player == SCISSORS and com == PAPER:
	res = '승리'
elif player == ROCK and com == SCISSORS:
	res = '승리'
elif player == PAPER and com == ROCK:
	res = '승리'
else:
	res = '패배'

print('player:', player, 'com:', com)
print(res)