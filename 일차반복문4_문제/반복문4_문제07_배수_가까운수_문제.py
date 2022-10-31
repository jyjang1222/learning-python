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
tmp = 0


while True:
	if i <= 100:
		num1 = i
	if i > 100:
		num2 = i
	i += 6

tmp = 100 - num1
	
if tmp < num2 - 100:
	print(tmp)
print(i)