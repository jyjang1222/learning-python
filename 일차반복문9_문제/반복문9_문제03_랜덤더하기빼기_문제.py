import random
'''
	[문제]
		숫자 5개를 랜덤으로 뽑고, 
		랜덤으로 더하기나 빼기를 한 총합을 구하려고 한다.
  
		변수 r 은 숫자를 표현하며, 변수 op는 기호를 표현한다.
		변수 r 에 랜덤숫자(1~9)를 5개를 뽑는다. 
		또 op변수는 더하기나 빼기를 뜻하는 랜덤숫자(0, 1)도 4개를 뽑는다. 
		(기호는 숫자보다 1개 적어야 한다.)
		op 변수의 0은 더하기고 1은 빼기이다. 
		
		[예시]
			r 은 3, 6, 5, 3 , 1이 나왔다고 가정하고,
			op 는 0, 1, 0, 1이 나왔다고 하면, 
	
			3 + 6 - 5 + 3 - 1 이된다. 
'''

r = 0
op = 0
sum = 0

i = 1
while i <= 5:
	r = random.randint(1, 9)
	print(r, end = " ")
	if op == 0:
		sum += r
	if op == 1:
		sum -= r
	if i == 5:
		print("총합:", sum)
		break
	op = random.randint(0, 1)
	if op == 0:
		print("+", end = " ")
	else:
		print("-", end = " ")
	i += 1