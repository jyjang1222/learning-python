import random
'''
	[문제]
		3~6 사이의 랜덤 숫자 하나를 저장하고 그 숫자만큼 아래와 같은 규칙으로 출력하시오.
		단, 일차 반복문으로 출력하시오.
 	[예시]
		r = 6
	[출력]
		18 12 6
		17 11 5
		16 10 4
		15 9 3
		14 8 2
		13 7 1
'''

r = random.randint(3, 6)
print(r)

i = r * 3
cnt = 0
cnt2 = 0
while True:
	if cnt == r:
		break
	if cnt2 == 0:
		j = i
	print(j, end = " ")
	cnt2 += 1
	j -= r
	if cnt2 == 3:
		cnt2 = 0
		cnt += 1
		i -= 1
		print()
	
	
	

