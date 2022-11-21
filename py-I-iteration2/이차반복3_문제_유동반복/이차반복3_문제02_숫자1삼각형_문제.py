'''
	[문제]
		아래와 같이 삼각형을 출력하시오.
	[예시]
		1
		1 2
		1 2 3
		1 2 3 4
		1 2 3 4 5	
'''

for i in range(1, 6):
	for j in range(1, i + 1):
		print(j, end = " ")
	print()