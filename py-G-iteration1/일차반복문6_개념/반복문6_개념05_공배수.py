'''
[문제]
	12와 15의 공배수를 작은 것부터 순서대로 5개만 출력하시오.
[정답]
	60 120 180 240 300 
'''

# 풀이

num = 0
count = 0

while True:
	num += 12
	if num % 12 == 0 and num % 15 == 0:
		count += 1
		print(num, end = " ")
		if count == 5:
			break


# count = 0

# i = 12

# run = 1
# while run == 1:
# 	if i % 12 == 0 and i % 15 == 0:
# 		print(i, end=" ")
# 		count += 1

# 		if count == 5:
# 			run = 0
# 	i += 1

