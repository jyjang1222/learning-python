import random
'''
	[문제]
		3~6 사이의 랜덤 숫자 하나를 저장하고 그 숫자만큼 아래와 같은 규칙으로 출력하시오.
		단, 일차 반복문과 이차 반복문으로 출력하시오.
 	[예시]
		r = 6
	[출력]
		3 2 1
		6 5 4
		9 8 7
		12 11 10
		15 14 13
		18 17 16
'''

r = random.randint(3, 6)

# 1
cnt = 0
cnt2 = 0
i = 3
while True:
	if cnt == r:
		break
	if cnt2 == 0:
		j = i
	print(j, end = " ")
	cnt2 += 1
	j -= 1
	# 3번 출력후 줄바꿈 i += 3
	if cnt2 == 3:
		print()
		cnt2 = 0
		cnt += 1
		i += 3
	
	

print()
# 2
cnt = 0
i = 3
while True:
	if cnt == r:
		break
	cnt2 = 0
	j = i
	while True:
		if cnt2 == 3:
			break
		print(j, end = " ")
		cnt2 += 1
		j -= 1
	print()
	cnt += 1
	i += 3
