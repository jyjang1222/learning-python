import random
'''
	[문제]
		철수는 게임을 만들려고 한다.
		숫자 다섯 개를 랜덤(1~9사이의 숫자)으로 저장한다.
		각각의 숫자는 중복이 되면 안된다.

		각각의 숫자로 랜덤 조합을 4가지 만들어서
		numList에 저장하고, 전체 합을 출력하시오.
		랜덤 조합 역시 중복이 되면 안된다.
		[예]
			1, 3, 5, 7, 9 라고 했을 때
			[1] 13597
			[2] 51397
			[3] 37951
			[4] 91537

			정답 : 13597 + 51397 + 37951 + 91537 = 194482
'''
numList = []

while True:
	if len(numList) == 5:
		break
	r = random.randint(1, 9)
	chk = True
	for j in range(len(numList)):
		if numList[j] == r:
			chk = False
	if chk:
		numList.append(r)


print(numList)
print()

arr = []

while True:
	if len(arr) == 5:
		break
	tmp = []
	# 로또생성
	for i in range(len(numList)):
		r = random.randint(0, len(numList) - 1)
		tmp.append(numList[r])
	# 중복체크
	chk = True
	for i in range(len(tmp)):
		for j in range(len(tmp)):
			if i != j:
				if tmp[i] == tmp[j]:
					chk = False
	if chk:
		arr.append(tmp)
		

for i in range(len(arr)):
	print(arr[i])

sumArr = []

for i in range(len(arr)):
	sum = 0
	k = 1
	for j in range(len(arr[i])-1,-1,-1):
		sum += arr[i][j] * k
		k *= 10
	sumArr.append(sum)

print(sumArr)

total = 0

for i in sumArr:
	total += i

print(total)