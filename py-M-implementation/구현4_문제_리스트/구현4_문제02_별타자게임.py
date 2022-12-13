import random
"""
	* # 타자연습 게임[2단계]
	* 1. 문제를 섞는다.(shuffle)
	* 2. 순서대로 문제를 출제하고, 문제를 다 맞추면 게임 종료
	* 3. 단 문제를 출제할 때, 단어의 랜덤한 위치 한 곳만 *로 출력
	* 예)
	* 문제 : mys*l
	* 입력 : mysql	<--- 정답을 맞추면, 다음 문제 제시
	* 문제 : *sp
	* 입력 : jsp

"""
a = ["mysql" , "jsp" , "javascript" , "python" , "java"]

for i in range(100):
	r1 = random.randint(0, len(a)-1)
	r2 = random.randint(0, len(a)-1)

	tmp = a[r1]
	a[r1] = a[r2]
	a[r2] = tmp

print(a)

i = 0
while i < len(a):
	str = a[i]
	r = random.randint(0, len(str)-1)
	censoredStr = str.replace(str[r], '*')

	while True:
		print('문제:', censoredStr)
		answer = input('입력: ')

		if a[i] == answer:
			i += 1
			break