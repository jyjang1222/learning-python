'''
	[문제]
		계단이 50 계단이 있다. 철수는 제일 위 계단에 서 있다. 
		철수는 한 번에 두 계단씩 내려간다. 
		철수가 왼발로 디딘 계단을 출력하시오.
		아래 조건을 참고하시오.
		[1] 철수는 한 번에 두 계단씩 내려간다.
		[2] 철수는 왼발부터 내려간다.
		[3] 5번 출력할 때마다 다른 발을 출력하시오.
		
		48 44 40 36 32 
		30 26 22 18 14
		12 8  4
'''

철수위치 = 50
turn = True
count = 0


while 철수위치 > 0:
	if count % 5 == 0 and count != 0:  # 발바꿔서 출력
		print()
		turn = not(turn)
	if turn == True:  # 왼발
		if 철수위치 % 4 == 0:
			print("왼", 철수위치, end = " ")
			count += 1
	if turn == False:  # 왼발
		if 철수위치 % 4 == 2:
			print("우", 철수위치, end = " ")
			count += 1
	철수위치 -= 2