'''
	[문제]
		a리스트에서 혼자 있는 값만 제외하고 b에 추가하시오.
	[예시]
		[1,2,3,2,1] : b = [1,2,2,1]    # 3 삭제
		[1,3,4,4,2] : b = [4,4]        # 1,2,3 삭제
		[1,1,1,1,1] : b = [1,1,1,1,1]  # 없음
'''

a = [1,2,3,2,1]
a = [1,3,4,4,2]
a = [1,1,1,1,1]
a = [1,4,4,4,2]
b = []

for i in range(len(a)):
	chk = False
	for j in range(len(a)):
		if i != j:
			if a[i] == a[j]:
				chk = True
	if chk:
		b.append(a[i])

print(b)
