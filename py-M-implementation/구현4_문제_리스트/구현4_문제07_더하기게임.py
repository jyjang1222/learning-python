import random
"""
	[더하기게임]	
		1) 1~10 사이의 숫자를 랜덤으로 7개보여준다. (중복금지)
		2) 그안에서 3개의 인덱스를 고를수있게해준다. (중복금지)
		3) 숫자를 하나 제시하는데 인덱스3개의 값의 합이
		   제시된 숫자랑 같으면 정답. 
		   단, 정답은 여러개 일수있다. 
		4) 반드시 정답의 경우의 수는 있어야한다.	 
		   단! 중복으로 값을 고를순없다. 
		[예시]

		    보기  
      		a = [1,5,8,6,4,2,9]
		    r = 13	
		[정답] 
  			인덱스를 세개를 고른다. [0,2,4] 각각의 값은 이와 같다. [1 + 8 + 4] 합이 13이므로 정답	
		[주의]
		    인덱스를 이와같이 똑같은 자리는 고를수없다. [5,5,6] 
"""

a = []
r = 0

num = [1,2,3,4,5,6,7,8,9,10]
for i in range(100):
	r1 = random.randint(0, len(num)-1)
	r2 = random.randint(0, len(num)-1)

	tmp = num[r1]
	num[r1] = num[r2]
	num[r2] = tmp

# print(num)

for i in range(7):
	a.append(num[i])

print(a)

idxList = []
while True:
	chk = True
	idx = int(input('서로 다른 인덱스 3개를 골라주세요.\n'))
	for i in idxList:
		if i == idx:
			chk = False
	if chk:
		idxList.append(idx)
	else:
		print('중복된 인덱스입니다. 다시 선택해주세요.')
	if len(idxList) == 3:
		break

sum = 0
for i in idxList:
	sum += i
answer = int(input('인덱스 3개의 값의 합을 입력해주세요.\n'))
if sum == answer:
	print('sum:', sum, '정답입니다.')
else:
	print('sum:', sum, '오답입니다.')

print(idxList)