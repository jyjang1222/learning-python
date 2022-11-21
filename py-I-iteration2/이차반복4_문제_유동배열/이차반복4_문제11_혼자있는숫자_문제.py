'''
	[문제]
		a리스트에서 혼자있는 숫자만 출력하시오.
	[정답]
		20 50
'''

a = [10,20,30,40,40,10,30,10,50]

for i in range(len(a)):
	chk = True
	for j in range(len(a)):
		# 자기자신은 비교에서 제외
		if i != j:
			if a[i] == a[j]:
				chk = False
	if chk:
		print(a[i], end = " ")
