'''
	[문제]
		a리스트의 숫자를 하나씩 출력한다.
		단, 이미 출력이 되어 중복되는 숫자는 출력하지 마시오.
	[정답]
		1 2 3 4 100		
'''
a = [1,1,2,2,3,3,4,100,3]


for i in range(len(a)):
	chk = True
	# 현재인덱스i에서 이전 배열값 모두 비교
	for j in range(i):
		if a[i] == a[j]:
			chk = False
			break
	if chk:
		print(a[i], end = " ")



	
