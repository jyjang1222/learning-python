'''
	[문제]
		아래와 같이 삼각형을 출력하시오.
  
	[예시]
		********
		******
		****
		**
'''

cnt = 0
i = 8
while cnt < 4:
	j = 1
	while j <= i:
		print("*",end = "")
		j += 1
	print()
	cnt += 1
	i -= 2