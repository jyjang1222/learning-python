'''
	[문제]
		a리스트의 값 중 0을 제외한 모든 값을 왼쪽으로 모으시오.
 	[결과]
 		a = [2,3,4,5,0,0,0,0,0,0];
'''


a = [0,0,2,0,3,0,4,0,0,5]

index  = 0
for i in range(len(a)):
	if a[i] != 0:
		a[index] = a[i]
		a[i] = 0

		index += 1

print(a)