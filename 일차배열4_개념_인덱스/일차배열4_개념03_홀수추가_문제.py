'''
	[문제] 
		다음 리스트를 이용해서 a의 값 중 
		홀수만 b에 저장하고 출력하시오.
	[예]   
 		b = [ 49, 51, 17 ]
'''
a = [49, 2, 51, 22, 17]
b = []

for i in a:
	if i % 2 == 1:
		b.append(i)

print(b)