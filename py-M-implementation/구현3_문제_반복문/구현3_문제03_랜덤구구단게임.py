import random
"""		 
	[랜덤구구단 게임] (반복문사용)
		1. 랜덤구구단 게임을 10회 반복한다.
		2. 숫자 두개는 랜덤으로 출력된다. 
		3. 정답을 맞추면 1문제당 10점이다.
		4. 게임 종료 후, 성적을 출력한다.
		5. 단, 3번연속으로틀리면 즉시종료하며 0점이된다.
"""
score = 0
count = 0
for i in range(10):
	r1 = random.randint(2, 9)
	r2 = random.randint(2, 9)
	calc = r1 * r2
	print(r1, 'x', r2)
	answer = int(input('숫자입력\n'))
	if calc == answer:
		score += 10
		count = 0
	else:
		count += 1

	if count == 3:
		score = 0
		break

print(score)

