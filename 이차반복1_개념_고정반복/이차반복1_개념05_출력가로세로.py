import random
'''
	[문제]
		랜덤(3~6)숫자 두개를 저장하고 그 숫자만큼 아래와 같은 규칙 출력하시오.
		반복문으로 출력하시오.
 	
 	[예시1]
		r1 = 3
		r2 = 3
	[출력1]
		1 7 13
		3 9 15
		5 11 17

	[예시2]
		r1 = 5
		r2 = 4
	[출력2]
		1 7 13 19
		3 9 15 21
		5 11 17 23
        7 13 19 25
        9 15 21 27
'''

r1 = random.randint(3, 6)
r2 = random.randint(3, 6)
print(r1, r2)

cnt = 0

i = 1
while True:
	if cnt == r1:
		break
	j = i
	cnt2 = 0
	while cnt2 < r2:
		print(j, end = " ")
		cnt2 += 1
		j += 6
	print()
	cnt += 1
	i += 2
