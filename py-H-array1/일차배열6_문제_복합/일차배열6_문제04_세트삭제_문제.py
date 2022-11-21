import random
'''
	[문제]
		a리스트는 학생 번호와 점수 한 세트를 이루고 있다.		
		0 ~ 7 사이의 랜덤 숫자를 저장하고,
		해당 위치의 학생 번호와 그 점수를 삭제하시오.
	[예시]
		
'''
# 01 23 45 67
a = [1001, 40, 1002, 60, 1003, 65, 1004, 70]
r = random.randint(0, 7)

idx = 0
grade = 0

if r % 2 == 1:
	idx = a[r - 1]
	grade = a[r]
	# a.remove(a[r])
	# a.remove(a[r - 1])
else:
	idx = a[r]
	grade = a[r + 1]
	# a.remove(a[r])
	# a.remove(a[r])

print(r, idx, grade)

a.remove(idx)
a.remove(grade)

print(a)
