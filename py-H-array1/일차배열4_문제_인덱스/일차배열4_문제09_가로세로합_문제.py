'''
	[문제]	
		아래 a 리스트는 한 줄 리스트이지만 
		아래와 같이 사각형으로 놓였다고 했을 때,  
		[1] a 리스트의 가로 합은 garo 리스트에 저장하시오.
		[2] a 리스트의 세로 합은 sero 리스트에 저장하시오.
	[정답]
		garo = [10, 26, 42]
		sero = [15, 18, 21, 24]
'''	

a = [1, 2, 3, 4,
     5, 6, 7, 8,
     9, 10,11,12]

garo = [0, 0, 0]
sero = [0, 0, 0, 0]

count = 0
tmp = 0
j = 0

# 가로
for i in a:
	tmp += i
	count += 1
	if count == 4:
		garo[j] = tmp
		tmp = 0
		count = 0
		j += 1
		
print(garo)

# 세로
count2 = 0

for i in a: 
	sero[count2] += i
	count2 += 1
	if count2 == 4:
		count2 = 0
print(sero)