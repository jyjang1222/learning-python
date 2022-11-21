'''
	[문제]
		a리스트의 값을 b에 저장한다.
		단, 연속으로 중복되는 값은 한 개만 저장하고 나머지는 저장하지 않는다.
	[예시]
		b = [1,3,2,3,4,5,6]
'''
a = [1,1,1,3,3,3,3,2,2,3,3,3,4,5,6,6,6]
b = []


for i in a:
	chk = True
	cnt = 0
	for j in b:
		if i == j:
			cnt += 1
	if cnt == 2:
		chk = False
	if chk:
		b.append(i)

print(b)