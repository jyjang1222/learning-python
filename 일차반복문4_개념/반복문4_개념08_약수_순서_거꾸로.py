'''
[문제]
	852의 약수 중에서 큰 수부터 작은 수를 거꾸로 출력했을 때,
	다섯 번째 약수만 출력하시오.
[정답]
	142
'''

# 풀이

i = 1
j = 852
count = 0

while i <= 852:
	if 852 % j == 0:
		count += 1
		if count == 5:
			print(j)
			break
	j -= 1
	i += 1

# count = 0

# i = 852
# while i >= 1:
# 	if 852 % i == 0:
# 		count += 1

# 		if count == 5:
# 			print(i)

# 	i -= 1
