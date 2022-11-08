'''
	[문제]
		다음은 학생 번화와 점수의 한 세트이다.
		일등의 번호와 점수, 꼴등의 번호와 점수를 출력하시오.
	[정답]
		일등 = 1004 98
		꼴등 = 1002 11
'''


numberList = [1001, 1002, 1003, 1004, 1005]
scoreList = [87, 11, 45, 98, 23]

max = 0
min = 100
best = 0
worst = 0
count = 0

for i in scoreList:
	if max < i:
		max = i
		best = count
	if min > i:
		min = i
		worst = count
	count += 1

print(numberList[best], max)
print(numberList[worst], min)
	