'''
	  	[문제]
		 	아래 리스트를 아래와 같이 출력하시오.
		[결과]
			1234
			567
			89
			0
'''



a = [1,2,3,4,5,6,7,8,9,0]

count = 0
# i = 4
# while i >= 0:
# 	j = 1
# 	while j <= i:
# 		print(a[count], end = "")
# 		count += 1
# 		j += 1
# 	print()
# 	i -= 1

for i in range(4, 0, -1):
	j = 1
	for j in range(j, i + 1):
		print(a[count], end = "")
		count += 1
	print()