import random
'''
	[문제]
		2~1000 사이의 랜덤 숫자 하나를 저장한다.
		위 숫자 바로 다음 소수를 출력하시오.
	
	[예시1]
		r = 1000
		소수 = 1009	 
	[예시2]
		r = 500
	    소수 = 503
'''

r = random.randint(2, 1000)
# r = 727
print(r)
# chk = True
# cnt = 0
i = r + 1
while True:
	cnt = 0
	j = 2
	while j <= i:
		if i % j == 0:
			cnt += 1
		j += 1
	if cnt == 1:
		print(i)
		break
	i += 1


