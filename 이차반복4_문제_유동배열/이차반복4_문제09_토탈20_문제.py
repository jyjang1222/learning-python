import random
'''
	[문제]
		[1] a리스트에 1~10까지의 랜덤 숫자 3개를 저장 후 출력하시오.
		[2] 단, 숫자 3개는 서로 중복되면 안 된다. 
		[3] 숫자 3개의 합은 반드시 20이어야 한다. 
	[예시]
		[3, 10, 7] o 
		[5, 10, 5] x 
'''

a = [0,0,0]

while True:
	sum = 0
	i = 0
	while i < 3:
		chk = True
		r = random.randint(1, 10)
		for j in range(i + 1):
			if a[j] == r:
				chk = False
		if chk:
			a[i] = r
			i += 1

	for i in range(len(a)):
		sum += a[i]

	if sum == 20:
		print(a)
		break


