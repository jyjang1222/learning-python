import random
'''
	[문제]
		3~6 사이의 랜덤 숫자 하나를 저장하고 그 숫자만큼 아래와 같은 규칙으로 출력하시오.
		단, 일차 반복문과 이차 반복문으로 출력하시오.
 	[예시]
		r = 6
	[출력]
		6 5 4
		5 4 3
		4 3 2
		3 2 1
'''

r = random.randint(3, 6)
print(r)

# 1
i = r
cnt = 0
while True:
	if cnt == 0:
		j = i
	print(j, end = " ")
	if j == 1:
		break
	cnt += 1
	j -= 1
	if cnt == 3:
		cnt = 0
		print()
		i -= 1
	
print()
# 2
i = r
cnt2 = 0
while j >= 1:
	j = i
	while True:
		print(j, end = " ")
		cnt2 += 1
		j -= 1
		if cnt2 == 3:
			cnt2 = 0
			break
	# if j == 1:
	# 	break
	print()
	i -= 1
