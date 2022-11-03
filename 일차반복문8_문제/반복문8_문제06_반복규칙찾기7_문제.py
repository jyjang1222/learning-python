'''  	
	[문제]
		반복문을 10회 반복해서 아래와 같이 출력하시오.
		
		[예시]
			0 1
			1 2
			2 2
			3 3
			4 3
			5 3
			6 4
			7 4
			8 4
			9 4
'''

count = 0

i = 1
while i <= 4:
	j = 1
	while j <= i:
		print(count, i)
		count += 1
		j += 1
	i += 1