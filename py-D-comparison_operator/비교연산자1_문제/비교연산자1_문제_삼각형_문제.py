'''
	[문제]
		가로가 3이고 세로가 6인 
        삼각형 넓이가 홀수인지 구하시오.
		위내용을 비교연산자로 표현하시오.
    [정답]
        True
'''

가로 = 3
세로 = 6
넓이 = 가로 * 세로 / 2
print(넓이 % 2 == 1)