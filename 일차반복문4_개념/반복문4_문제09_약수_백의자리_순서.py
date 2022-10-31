'''
[문제]
	1980의 약수 중에서 순서대로 약수를 출력했을 때, 
	십의 자리가 9인 두 번째 약수를 출력하시오.
[정답]
	99
'''

# 풀이

i = 1
num = 1980
count = 0

while i <= num:
	if num % i == 0 and i % 100 // 10 == 9:
		count += 1
		if count == 2:
			print(i)
			break
	i += 1











# count = 0

# i = 1
# while i <= 1980:
# 	if 1980 % i == 0:
# 		if i % 100 // 10 == 9:
# 			count += 1

# 			if count == 2:
# 				print(i)

# 	i += 1