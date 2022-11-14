import random
'''
	[문제]
		아래와 같이 삼각형을 출력하시오.
	[예시]
		1
		1 2
		1 2 3
		1 2 3 1
		1 2 3 1 2
		1 2 3 1 2 3
		1 2 3 1 2 3 1
		1 2 3 1 2 3 1 2
		1 2 3 1 2 3 1 2 3
		1 2 3 1 2 3 1 2 3 1
'''

r = random.randint(1, 9)
cnt = 0

# while True:
# 	i = 1
# 	if cnt == r:
# 		break
# 	j = i
# 	while True:
# 		print(j, end = " ")
# 	cnt += 1
# 	i += 1