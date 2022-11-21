import random
'''
	[문제]
		2~100 사이의 랜덤 숫자 하나를 저장하고, 
		2부터 그 숫자 사이의 모든 소수의 개수를 출력하시오.

	[예시]
		r = 20
	 	소수 = 2, 3, 5, 7, 11, 13, 17, 19
		개수 = 8
'''

r = random.randint(2, 100)
print(r)

cnt2 = 0

i = 2
for i in range(r + 1):
	cnt = 0
	j = 2
	while j <= i:
		if i % j == 0:
			cnt += 1
		j += 1
	if cnt == 1:
		cnt2 += 1
		print(i, end = " ")

print()
print(cnt2)