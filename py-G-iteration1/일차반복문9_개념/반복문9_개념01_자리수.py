import random

'''
[문제]
	1 ~ 2000 사이의 랜덤숫자를 저장하고, 
	자리수가 얼마인지 출력하시오.
[예시]
	969
	3자리 수
'''


'''
num // 1000 != 0  4
num // 100 != 0  3
num // 10 != 0  2
'''

# 1차 풀이
num = random.randint(1, 2000)

i = 1
j = 1000
count = 4

while i <= 4:
	if num // j != 0:
		print(num, count, "자리 수")
		break
	if num // j == 0:
		count -= 1
	i += 1
	j /= 10
	


'''
# 969 // 10 = 96		1
# 96 // 10 = 9		2
# 9 // 10 = 0			3
'''

# num = random.randint(1, 2000)
# print("num = ", num)

# temp = num

# count = 0

# run = 1
# while run == 1:
# 	temp = temp // 10
# 	print(temp)
# 	count += 1

# 	if temp == 0:
# 		run = 0
# print(count)












