'''
[문제]
	a중학교 1학년 입학하는 학생들은 8줄, 12줄, 18줄로 세워도
	항상 5명이 남을 때,	1학년 전체 학생 수를 구하시오.
	(학생 수는 200명 이상 250명 미만)
[정답]
	221
'''
전체학생수 = 0

i = 200

run = 1
while run == 1:
	if i % 8 == 5 and i % 12 == 5 and i % 18 == 5:
		전체학생수 = i
		run = 0
	i += 1
print(전체학생수)
