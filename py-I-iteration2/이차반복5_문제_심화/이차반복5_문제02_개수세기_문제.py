'''
	[문제]
		a리스트의 값을 중복없이 value에 저장한다.
		그리고 중복되는 개수를 count에 저장한다.
	[정답]
		value = [10,20,30,100]
		count = [2,3,5,1]
'''

a = [10, 20, 30, 30, 100, 10, 30, 30, 20, 30, 20]

value = []
count = []

for i in a:
	chk = True
	for j in value:
		if i == j:
			chk = False
	if chk:
		value.append(i)
	
print(value)

for i in value:
	cnt = 0
	for j in a:
		if i == j:
			cnt += 1
	count.append(cnt)

print(count)