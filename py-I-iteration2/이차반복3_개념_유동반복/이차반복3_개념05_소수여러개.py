import random
'''
	[문제]
		2~100 사이의 랜덤 숫자 하나를 저장하고, 
		2부터 그 숫자 사이의 모든 소수를 출력하시오.

	[예시]
		r = 20
	 	소수 = 2, 3, 5, 7, 11, 13, 17, 19	
'''

r = random.randint(2, 100)
print(r)


for i in range(2, r + 1):
	cnt = 0
	# 1은 모든수의 약수이므로 제외
	for j in range(2, i + 1):
		if i % j == 0:
			cnt += 1
	if cnt == 1:
		print(i, end = " ")











# 틀린정답
# r = random.randint(2, 100)
# print("r =", r)

# i = 2
# while i <= r:
# 	if r % i == 0:
# 		print(i, end=" ")
# 	i += 1