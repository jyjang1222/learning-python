import random
'''
	[문제]		
		[1] com리스트에 0~9사이의 랜덤 숫자 3개를 저장하되 중복 값이 없어야 한다.
		[2] me리스트에 0~9사이의 랜덤 숫자 3개를 저장하되 중복 값이 없어야 한다.
		[3] com과 me 를 비교해서 숫자가 같고 자리도 같으면 strike + 1
		[4] com과 me 를 비교해서 숫자가 같고 자리가 틀리면 ball + 1
		[5] 사용자에게 strike와 ball 개수를 출력해 보여준다.
		
		com은 고정이고 [2] ~ [5]를 반복하면서 strike가 3이 되면 종료한다.
'''
com = [0, 0, 0]
me = [0, 0, 0]


while True:
	strike = 0
	ball = 0
	# com숫자 3개 저장
	i = 0
	while i < 3:
		bool = True
		r = random.randint(0, 9)

		for j in range(i + 1):
			if r == 0 and com[j] == 0:
				break
			if com[j] == r:
				bool = False
		if bool:
			com[i] = r
			i += 1

	# me숫자 3개 저장
	j = 0
	while j < 3:
		bool = True
		r = random.randint(0, 9)

		for k in range(j + 1):
			if r == 0 and me[k] == 0:
				break
			if me[k] == r:
				bool = False
		if bool:
			me[j] = r
			j += 1

	for i in range(len(com)):
		if com[i] == me[i]:
			strike += 1
		else:
			for j in range(len(com)):
				if com[i] == me[j]:
					ball += 1
	print(com, me, strike, ball)

	if strike == 3:
		break

print(com, me)