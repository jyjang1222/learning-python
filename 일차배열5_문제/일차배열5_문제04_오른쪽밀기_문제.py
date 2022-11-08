'''
	[문제]
		a리스트의 값중 0을 제외하고 모든값을 오른쪽으로 모으시오.
 	[결과]
 		a = [0,0,0,0,0,0,2,3,4,5];
'''


a = [1,0,2,0,3,0,4,2,0,5]

idxEnd = len(a) - 1
count = 0
tmp = 0

for i in range(len(a)):
	if a[idxEnd - i] != 0:
		tmp = a[idxEnd - count]
		a[idxEnd - count] = a[idxEnd - i]
		a[idxEnd - i] = tmp
		count += 1
print(a)