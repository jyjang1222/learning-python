import random
'''
	[문제]
		랜덤으로 (1~4)를 저장하고
		아래와 같은 경우로 리스트에 저장하시오.
	[예]
		[1 번 선택시] 
		123  n += 3 n += 1
		654  n += 3 n -= 1
		789  n += 3 n += 1
		
		[2 번 선택시]
		761
		852
		943
		
		[3번 선택시]		
		987
		456
		321
		
		[4번 선택시]	
		349
		258
		167
'''
snake = []
snake = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

r = random.randint(1, 4)
# r = 4

n = 1
if r == 1:
	# 3행까지
	for i in range(3):
		# 홀수행이면
		if i % 2 == 0:
			for j in range(3):
				snake[i][j] = n
				if j == 2:
					break
				n += 1
		# 짝수행이면
		if i % 2 == 1:
			for j in range(3):
				snake[i][j] = n
				if j == 2:
					break
				n -= 1
		n += 3

n = 1
if r == 2:
	for i in range(len(snake) - 1, -1, -1):
		# 홀수행이면
		if i % 2 == 0:
			for j in range(3):
				snake[j][i] = n
				if j == 2:
					break
				n += 1
		# 짝수행이면
		if i % 2 == 1:
			for j in range(3):
				snake[j][i] = n
				if j == 2:
					break
				n -= 1
		n += 3

n = 9
if r == 3:
	for i in range(3):
		# 홀수행이면
		if i % 2 == 0:
			for j in range(3):
				snake[i][j] = n
				if j == 2:
					break
				n -= 1
		# 짝수행이면
		if i % 2 == 1:
			for j in range(3):
				snake[i][j] = n
				if j == 2:
					break
				n += 1
		n -= 3

n = 9
if r == 4:
	for i in range(len(snake) - 1, -1, -1):
		# 홀수행이면
		if i % 2 == 0:
			for j in range(3):
				snake[j][i] = n
				if j == 2:
					break
				n -= 1
		# 짝수행이면
		if i % 2 == 1:
			for j in range(3):
				snake[j][i] = n
				if j == 2:
					break
				n += 1
		n -= 3

print(r)
print(snake)
for i in range(len(snake)):
	print(snake[i])