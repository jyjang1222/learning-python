'''
	  	[문제]
		 	아래 리스트를 아래와 같이 출력하시오.
		[결과]
			1
			23
			456
			7890
'''

# a = [1,2,3,4,5,6,7,8,9,0]
a = []
for i in range(5):
	for j in range(1, 10):
		a.append(j)
	a.append(0)

count = 0

i = 1
while True:
	j = 1
	# while j <= i:
	# 	print(a[count], end = "")
	# 	count += 1
	# 	j += 1
	# 	if count >= len(a):
	# 		break
	for j in range(j, i + 1):
		print(a[count], end = "")
		count += 1
		if count >= len(a):
			break
	if count >= len(a):
		break
	print()
	i += 1




