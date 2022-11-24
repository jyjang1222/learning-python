'''
	[달팽이]
		a에 아래와같이 저장후 출력하시오..
	  
	  
	1 	2	3	4	5	
	16	17	18	19	6	
	15	24	25	20	7	
	14	23	22	21	8	
	13	12	11	10	9
'''
a = []

for i in range(5):
	tmp = []
	for j in range(5):
		tmp.append(0)
	a.append(tmp)

y = 0
x = 0
a[x][y] = 1

chk = True
cnt = 0
n = 2
while n <= 25:
	if chk:
		if x + 1 < len(a) and a[y][x+1] == 0:
			x += 1
			if x == len(a) - 1 or a[y][x+1] != 0:
				cnt += 1
		elif y + 1 < len(a) and a[y+1][x] == 0:
			y += 1
			if y == len(a) - 1 or a[y+1][x] != 0:
				cnt += 1
	else:
		if x - 1 >= 0 and a[y][x-1] == 0:
			x -= 1
			if x == 0 or a[y][x-1] != 0:
				cnt += 1
		elif y - 1 >= 0 and a[y-1][x] == 0:
			y -= 1
			if y == 0 or a[y-1][x] != 0:
				cnt += 1
	a[y][x] = n
	if cnt == 2:
		chk = not(chk)
		cnt = 0
	n += 1

for i in range(len(a)):
	print(a[i])