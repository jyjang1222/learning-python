'''
	[문제]
		아래와 같이 삼각형을 출력하시오.
	[예시]
		1 2 3 4 5 6 7 8
  		1 2 3 4 5 6
		1 2 3 4
		1 2
'''

cnt = 0
i = 8
while cnt < 4:
	j = 1
	while j <= i:
		print(j, end = " ")
		j += 1
	print()
	cnt += 1
	i -= 2