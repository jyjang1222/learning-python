import random
"""
	[홀짝게임]		  
		[1] 1~10사이의 숫자를 랜덤으로 저장한다.
		[2] 문자로 입력을 "홀" 또는 "짝" 을 입력한다. 
		[3] 홀짝을 맞추는게임이다. 
		[4] 기본금은 3000원을 가지고시작한다. 정답을 맞추면 700원 이득을 보고,틀리면 1000원 손해를 본다.
		[5] 매게임이 끝날때마다 새로운메뉴 [1.한번더][2.종료] 를 보여준다.   
		[6] 게임종료후 남은자금을 출력하시오.
		[7] 돈이 부족하면 게임은 자동종료된다. 
 
"""


ODD = '홀'
EVEN = '짝'

gold = 3000
res = ODD

while True:
	while True:
		userInput = input('홀짝입력\n')
		if userInput == ODD or userInput == EVEN:
			break

	r = random.randint(1, 10)
	if r % 2 == 0:
		res = EVEN

	if userInput == res:
		gold += 700
	else:
		gold -= 1000
	print('게이머:', userInput, '결과:', res)
	print('남은돈:', gold)
	userInput2 = int(input('[1.한번더][2.종료]\n'))
	if userInput2 == 1:
		continue
	else:
		break