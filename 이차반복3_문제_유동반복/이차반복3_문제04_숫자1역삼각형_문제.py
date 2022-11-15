'''
	[문제]
		아래와 같이 삼각형을 출력하시오.
	[예시]
		12345
		1234
		123
		12
		1
'''

for i in range(6, 0, -1):
	for j in range(1, i + 1):
		print(j, end = "")
	print()