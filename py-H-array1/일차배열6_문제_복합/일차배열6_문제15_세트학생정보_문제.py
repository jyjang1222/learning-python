'''
	[문제]
		아래 배열은 3명의 학생 데이터이다.		
		각 학생은 3개씩 데이터로 표현한다. 
		맨 앞은 번호, 그다음은 국어점수, 그다음은 수학점수이다.					
		(예) 
			1001번, 국어 100, 수학 20
			1002번, 국어 32,  수학 54
			1003번  국어 34,  수학 65	

		[1] 전체 평균을 출력하시오.
		[2] 국어 1등 학생을 출력하시오.
		[3] 수학 1등 학생을 출력하시오.
		[4] 전체 1등 학생을 출력하시오.
'''

a = [1001, 100, 20, 1002, 32, 54, 1003, 34, 65]

avg = 0
국어 = 0
math = 0
총인원 = len(a) // 3
국어avg = 0
수학avg = 0
tmp = 0
tmp2 = 0
국어max = 0
mathMax = 0

for i in range(len(a)):
	if i % 3 == 1:
		tmp += i
		if 국어max < a[i]:
			국어max = a[i]
	if i % 3 == 2:
		tmp2 += i
		if mathMax < a[i]:
			mathMax = a[i]

국어avg = round(tmp / 총인원, 2)
수학avg = round(tmp2 / 총인원, 2)
# print(국어max, mathMax)

국어best = 0
mathBest = 0

for i in range(len(a)):
	if a[i] == 국어max:
		국어best = a[i - 1]
	if a[i] == mathMax:
		mathBest = a[i - 2]

print(국어best, mathBest)