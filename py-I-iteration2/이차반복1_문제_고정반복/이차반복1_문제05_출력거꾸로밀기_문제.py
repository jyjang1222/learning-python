import random
'''
	[문제]
		3~6 사이의 랜덤 숫자 하나를 저장하고 그 숫자만큼 아래와 같은 규칙으로 출력하시오.
		단, 일차 반복문과 이차 반복문으로 출력하시오.
 	[예시]
		r = 6
	[출력]
		3 2 1
		4 3 2
		5 4 3
		6 5 4
'''

r = random.randint(3, 6)
print(r)

# 1
i = 3
cnt = 0
while i <= r:
	if cnt == 0:
		j = i
	print(j, end = " ")
	cnt += 1
	j -= 1
	if cnt == 3:
		cnt = 0
		print()
		i += 1
	# if i == r:
	# 	break
	
print()
# 2
i = 3
while True:
	for j in range(i, i - 3, -1):
		print(j, end = " ")
	if i == r:
		break
	print()
	i += 1

