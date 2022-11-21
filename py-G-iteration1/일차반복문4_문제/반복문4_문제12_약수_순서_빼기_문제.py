'''
	[문제] 
		100의 약수 중에서 
        5번째 약수에서 2번째 약수를 뺀 값을 구하시오.
	[정답]
		8
'''

i = 1
count = 0
num = 100
num2 = 0
num3 = 0

while i <= num:
	if num % i == 0:
		count += 1
		if count == 2:
			num2 = i
		if count == 5:
			num3 = i
			print(num3 - num2)
			break
	i += 1