import random
'''
	[문제] 
		0~10 사이의 랜덤 숫자를 다섯 번 반복해서 저장하고
		그 랜덤 숫자만큼 * 을 출력하시오.
  
	[예]
		3   : ***
		10  : **********
		5   : *****
		6   : ******
		0   : 
		1   : *	
'''

arr = []

for i in range(5):
	r = random.randint(0, 10)
	arr.append(r)

print(arr)

for i in range(len(arr)):
	print(arr[i], end = " : ")
	for j in range(arr[i]):
		print("*", end = "")
	print()