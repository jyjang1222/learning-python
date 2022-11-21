'''
	[문제]
		a리스트와 b리스트의 값들이 각각 값과 개수가 똑같은지 확인한다.
		똑같으면 "같음", 아니면 "다름"을 출력하시오.
		위치는 상관없이 각각의 숫자의 개수가 일치하면 "같음"이다. 
	[정답]
'''
a = [10, 20, 30, 10, 20, 30]
a = [10, 20, 30, 10, 20, 30, 10]
b = [30, 20, 10, 20, 30, 10]
b = [30, 20, 10, 20, 30, 10, 20]
c = []
d = []

i = 10
while i <= 30:
	cnt1 = 0
	cnt2 = 0
	for j in a:
		if i == j:
			cnt1 += 1
	c.append(cnt1)
	for j in b:
		if i == j:
			cnt2 += 1
	d.append(cnt2)
	i += 10

print(c)
print(d)

j = 10
for i in range(len(c)):
	if c[i] == d[i]:
		print(j, "일치")
	else:
		print(j, "불일치")
	j += 10
		