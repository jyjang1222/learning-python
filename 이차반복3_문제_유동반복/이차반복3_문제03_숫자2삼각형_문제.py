import random
'''
	[문제]
		아래와 같이 삼각형을 출력하시오.
	[예시]
		1
		1 2
		1 2 3
		1 2 3 1
		1 2 3 1 2
		1 2 3 1 2 3
		1 2 3 1 2 3 1
		1 2 3 1 2 3 1 2
		1 2 3 1 2 3 1 2 3
		1 2 3 1 2 3 1 2 3 1
'''

r = random.randint(1, 9)
r = 9

for i in range(r):
	n = 1
	for j in range(i):
		print(n, end = " ")
		n += 1
		if n > 3:
			n = 1
	print()