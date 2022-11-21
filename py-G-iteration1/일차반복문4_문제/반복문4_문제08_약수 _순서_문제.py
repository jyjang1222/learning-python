'''
	[문제]
	  	745의 약수 중에서 작은 수부터 출력했을 때, 
		세 번째 약수만 출력하시오.
	[정답]
		149
'''

i = 1
count = 0

while i <= 745:
	if 745 % i == 0:
		count += 1
		if count == 3:
			print(i)
			break
	i += 1