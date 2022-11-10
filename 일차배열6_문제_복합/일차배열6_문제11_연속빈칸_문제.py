import random
'''
	[문제]
		철수네 공장의 창고를 아래 a리스트로 표현하였다.
		1은 물건이 차 있는 상황이고 0은 비어있는 상황이다.
		랜덤(1~5)으로 물건 크기를 입력받고 창고에 저장 후 출력하시오.
		저장할 수 없으면 "창고 부족"이라고 출력하시오.
		단, 물건은 앞에서부터 채워나간다.
	[예]
		r = 3
  		[0,1,0,0,0,1,0,0] : [0,1,1,1,1,1,0,0]
    
		r = 4
		[0,1,0,0,0,1,0,0]  : "창고부족"
'''
a = [0,1,0,0,0,1,0,0]
a = [0,1,0,0,0,1,0,0,0,0,1,0,0,1]
size = random.randint(1, 5)
size = 4

idx = 0
empty = 0
for i in range(len(a) - 1):
	# 0 나올때 idx
	if a[i] == 0:
		idx = i
	# 남은공간이 사이즈보다 같거나커야 체크 가능
	if (len(a) - 1) - idx >= size:
		# 남은공간체크
		for j in range(size):
			if a[idx + j] == 0:
				empty += 1
			else:
				empty = 0
				break
	if empty >= size:
		break

# 사이즈보다 남은공간이 같거나크다면
if empty >= size:
	# 0나온 idx부터 1로 채움
	for i in range(size):
		a[idx + i] = 1
else:
	print("공간부족")

print(size, a)

