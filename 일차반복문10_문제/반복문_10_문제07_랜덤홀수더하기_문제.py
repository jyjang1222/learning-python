import random
'''
	[문제]
		랜덤으로 2~5 를 저장하고, 
		랜덤숫자의 개수만큼 숫자를 더하는 문제와 답을 만들어 출력하시오..
		단 더하기 할 숫자들은 1~9사이의 홀수인 랜덤숫자여야 한다. 
		
		아래 [출력] 뒤에 나오는 모양과 똑같은 모양으로 출력한다. 
		(단, 숫자는 랜덤이므로 숫자는 다르게 나올 수 있다.)
			
		[예시1]		  		
			랜덤 ==> 3
			[출력] 5 + 3 + 1 = 9
			
		[예시2]
			랜덤 ==> 5
			[출력] 1 + 5 + 3 + 7 + 1 = 17
'''

r = 0
op = 1
sum = 0
num = random.randint(2, 5)

i = 1
while i <= num:
	r = random.randint(1, 9)
	print(r, end = " ")
	if op % 2 == 1:
		sum += r
	if op % 2 == 0:
		sum -= r
	if i == num:
		print("총합:", sum)
		break
	op = random.randint(1, 9)
	if op % 2 == 1:
		print("+", end = " ")
	else:
		print("-", end = " ")
	i += 1