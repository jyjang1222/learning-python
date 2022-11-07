import random
'''
	[문제]
		공간이 10개인 a리스트가 있다. 
		랜덤(0~9)로 시작 인덱스를 저장한다.
		랜덤(1~10)로 개수를 저장한다.
		시작 인덱스부터 개수만큼 거꾸로 숫자를 채워나간다.
		채우는 숫자는 1부터 1씩 증가한다.
		
	[예시]
		ranIndex = 3 
		ranCount = 7		
  		a = [4,3,2,1,0,0,0,7,6,5]  
  			- 인덱스 3부터 7개를 채운다. 
	

'''

a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
r1 = random.randint(0, 9)
r2 = random.randint(1, 10)
idx = r1
n = r2 + 1

for i in range(1, n):
	a[idx] = i
	idx -= 1
	if idx < 0:
		idx = len(a) - 1

print(r1, r2, a)

