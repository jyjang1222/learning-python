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
size = random.randint(1, 5)
size = 3

idx = 0
count = 0
for i in range(len(a) - 1):
	# 0 나올때 idx
	if a[i] == 0:
		idx = i
		# 남은공간체크
		# 남은공간이 사이즈보다 커야 체크 가능
		if len(a) - 1 - idx >= size:
			for j in range(size + 1):
				if a[idx + j] == 0:
					count += 1
				else:
					break
		# 사이즈보다 남은공간이 같거나크다면
		if count >= size:
			# 0나온 idx부터 1로 채움
			for k in range(size):
				a[idx + k] = 1
				print(a)
		# 사이즈보다 남은공간이 작다면
		else:
			# 다음 0을 찾아서 다음 반복으로
			continue
	else:
		pass

# print(size, a)

