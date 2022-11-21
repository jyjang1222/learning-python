'''
	[문제] 
  		6의 배수를 순차적으로 검사한다. 
  		그중 100에 가장 가까운 수를 출력하시오. 
 	[정답]
		102
'''

i = 6
num1 = 0
num2 = 0

while True:
	if i <= 100:
		num1 = i
	if i > 100:
		num2 = i
		break
	i += 6

if num2 - 100 > 100 - num1:
	print(num1)
else:
	print(num2)