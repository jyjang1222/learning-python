import random
"""
	* # 타자연습 게임[1단계]
	* 1. 문제를 섞는다.(shuffle)
	* 2. 순서대로 문제를 출제하고, 문제를 다 맞추면 게임 종료
	* 예)
	* 문제 : mysql
	* 입력 : mydb
	* 문제 : mysql
	* 입력 : mysql	<--- 정답을 맞추면, 다음 문제 제시
	* 문제 : jsp

"""
a = ["mysql" , "jsp" , "javascript" , "python" , "java"]


for i in range(100):
	r1 = random.randint(0, len(a)-1)
	r2 = random.randint(0, len(a)-1)
	tmp = 0

	tmp = a[r1]
	a[r1] = a[r2]
	a[r2] = tmp

print(a)

i = 0
while True:
	quiz = a[i]
	answer = input('문제: ' + quiz + '\n입력: ')

	if quiz == answer:
		if i == len(a) - 1:
			break
		i += 1

