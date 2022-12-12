import random
"""
	[정답]
	[홀짝 게임]
		1. 1~10개의 숫자중 랜덤으로 한개의 숫자를 저장한다.
		2. [1.홀수][2.짝수] 선택지를 보여준다.
		3. 사용자는 선택지를 고르고 "정답" , "오답" 을 출력한다.
"""

r = random.randint(1, 10)

while True:
	userInput = int(input('1.홀수 2.짝수\n'))
	if userInput == 1 or userInput == 2:
		break
print(r)
if r % 2 == 1:
	if userInput == 1:
		print('정답')
	else:
		print('오답')
if r % 2 == 0:
	if userInput == 2:
		print('정답')
	else:
		print('오답')