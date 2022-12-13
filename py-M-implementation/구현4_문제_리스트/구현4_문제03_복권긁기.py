import random
"""
	[복권긁기]
		[1] a 리스트에 숫자7을 3개 , 숫자 1을 4개를 저장한다. 
		[2] 위치는 랜덤으로 저장한다.
		[3] 사용자는 인덱스로 위치 3개를 선택할수있다. 
		[4] 전부 7이면 당첨 아니면 꽝 출력 

"""
a = [1,1,1,1,7,7,7]

for i in range(100):
	r1 = random.randint(0, len(a)-1)
	r2 = random.randint(0, len(a)-1)

	tmp = a[r1]
	a[r1] = a[r2]
	a[r2] = tmp

print(a)

chk = True

for i in range(3):
	idx = int(input('인덱스번호를 입력하세요 0 ~ 6\n'))
	if a[idx] != 7:
		chk = False

print(chk)