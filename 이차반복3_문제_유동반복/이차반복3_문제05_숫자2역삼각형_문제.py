'''
	[문제]
		아래와 같이 삼각형을 출력하시오.
	[예시]
		123123
		12312
		1231
		123
		12
		1
'''


for i in range(6):
	n = 1
	for j in range(6 - i):
		print(n, end = "")
		n += 1
		if n > 3:
			n = 1
	print()