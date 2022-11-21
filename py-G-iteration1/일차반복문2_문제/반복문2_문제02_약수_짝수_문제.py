'''
	[문제] 
		48의 약수 중 짝수만 출력하시오.
	[정답]
		2
		4
		6
		8
		12
		16
		24
		48
'''

i = 2
num = 48

while i <= num:
	if num % i == 0:
		print(i)
	i += 2