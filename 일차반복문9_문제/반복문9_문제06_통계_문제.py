import random
'''
	[문제]
		1. 10회 반복을 한다.
		2. 0~100 사이의 랜덤 숫자를 출력한다. (학생 점수)
		3. 번호는 1번부터 시작한다. 번호와 점수를 출력한다. 
		4. 성적이 60점 이상이면 합격생이다. 
		   합격생은 점수 옆에 [합격]을 불합격생은 [불합격]을 출력한다. 
		5. 전교생(10명)의 총점과 평균을 출력한다.
		6. 1등의 번호와 점수를 출력한다.
'''
전교생 = 10
score = 0
total = 0
best = 0
max = 0

i = 1
while i <= 전교생:
	score = random.randint(0, 100)
	total += score
	if score > max:
		max = score
		best = i
	if score >= 60:
		print("합격", end = " ")
	else:
		print("불합격", end = " ")
	print(i, score)
	i += 1

avg = round(total / 전교생, 2)
print(total, avg)
print(best, max)