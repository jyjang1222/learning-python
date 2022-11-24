'''
	[문제]
		위 데이터는 학생 4명의 데이터이다.
		순서대로 [번호], [국어], [수학], [영어], [등수]의 데이터이다. 		
		이제 등수를 넣어야한다. 각 과목별 등수별로 점수를 매기고 
		각 점수들의 합이 가장적은 학생이 1등이다. 
		총합이 같으면 같은 등수이다. 

		1번학생은 국어 4등, 수학3등, 영어2등으로 점수는 9점이다. 
		2번학생은 국어 3등, 수학1등, 영어3등으로 점수는 7점이다.
		3번학생은 국어 2등, 수학4등, 영어1등으로 점수는 7점이다.
		4번학생은 국어 1등, 수학2등, 영어4등으로 점수는 7점이다.

		1등은 3명, 4등은 1명이다. 
	[정답]
		[1001, 20, 43, 54, 4],
		[1002, 21, 73, 44, 1],
		[1003, 65, 13, 55, 1],
		[1004, 76, 63,  4, 1]
'''
score = [
			[1001, 20, 43, 54, 0],
			[1002, 21, 73, 44, 0],
			[1003, 65, 13, 55, 0],
			[1004, 76, 63,  4, 0]
		]
		# 01 11 21 31
		# ...
		# 03 13 23 33

gradeList = []

# 1 10 10 13
for i in range(len(score)):
	tmp = []
	for j in range(1, 4):
		# tmp = score[i][j]
		# 등수 체크
		grade = 1
		for m in range(len(score)):
			if score[m][j] > score[i][j]:
				grade += 1
		tmp.append(grade)
	gradeList.append(tmp)

for i in range(len(gradeList)):
	print(gradeList[i])

total = []

for i in range(len(gradeList)):
	sum = 0
	for j in range(len(gradeList[i])):
		sum += gradeList[i][j]
	total.append(sum)


print(total)

for i in range(len(total)):
	grade = 1
	for j in range(len(total)):
		if total[i] > total[j]:
			grade += 1
	score[i][4] = grade

for i in range(len(score)):
	print(score[i])