'''
	[문제]
		a와 b 두 리스트를 비교해서 서로 겹치지 않는 값을 
		temp에 저장하고 출력하시오.
	[정답]
		temp = [6, 4, 20, 3, 17, 13, 7]
'''
a = [16,  5, 11, 6, 19, 12, 18,  4, 20, 3]
b = [17, 11, 19, 5, 13, 18, 16, 12, 11, 7]
temp = []

for i in range(len(a)):
	bool = True
	for j in range(len(a)):
		if a[i] == b[j]:
			bool = False
	if bool:
		temp.append(a[i])

for i in range(len(a)):
	bool = True
	for j in range(len(a)):
		if b[i] == a[j]:
			bool = False
	if bool:
		temp.append(b[i])

print(temp)