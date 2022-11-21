'''
	[문제]
		아래 리스트 두 개를 합치고 오름차순으로 정렬하시오. 
	[정답]
		[1, 2, 3, 5, 7, 8, 9, 10, 12, 15, 19, 20]
'''

a = [9,10,3,2,20,19]
b = [15,12,1,5,7,8]
c = []

for i in b:
	a.append(i)

tmp = 0
minIdx = 0

for i in range(len(a)):
	minIdx = i
	tmp = a[i]
	for j in range(i, len(a)):
		if a[j] < a[minIdx]:
			# min = a[j]
			minIdx = j
	print(a, minIdx)
	a[i] = a[minIdx]
	a[minIdx] = tmp

print(a)
