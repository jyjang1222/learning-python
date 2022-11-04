'''
	[문제] 
		a리스트 안에 1 또는 7을 랜덤으로 7개 추가 후 출력하시오. 
		단, 7의 개수는 3개만 추가하고, 
		1의 개수는 4개만 추가한다.
		
	[예]
		정답 [ 1, 7, 7, 1, 1, 7, 1]  # 개수가 맞다. 
		오답 [ 7, 1, 1, 7, 1, 1, 1]  # 7이 두개이다.
			
'''
import random

a = []

count1 = 0
count7 = 0

while True:
	if count1 + count7 == 7:
		break

	r = random.randint(0, 1)

	if r == 0 and count7 <= 3:
		a.append(7)
		count7 += 1
	elif r == 1 and count1 <= 4:
		a.append(1)
		count1 += 1
print(a)


    
