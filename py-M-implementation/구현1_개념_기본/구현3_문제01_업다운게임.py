import random
"""
	[Up & Down 게임]
		1. com 은 랜덤으로 1~100사이를 저장한다.
		2. me 는 1~100사이를 입력한다. 	 
		3. com 과 me 를 비교해서 com 크면 "크다" , com 이작으면 "작다" 힌트제공 
		4. 정답을 맞출때까지 반복한다. 
		5. 6번 안에 맞추지 못하면 gameover
"""

com = random.randint(1, 100)

i = 0
limit = 6
while i < limit:
	me = int(input('수를 입력하세요. '))
	if me == com:
		print(com, me, '정답!')
		break
	if me > com:
		print('Down!')
	if me < com:
		print('Up!')
	i += 1
	if i == limit:
		print(com, 'gameover')
