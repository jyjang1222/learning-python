import random
'''
	[문제] 
		1~45사이의 랜덤값 6개를 lotto에 저장하려 한다.
		단, 중복되는 숫자는 없어야 하며,
		내림차순 정렬 후 출력하시오.
	[예시]
        [40, 38, 27, 26, 18, 5]
'''
lotto = []
r = random.randint(1, 6)
lotto.append(r)


i = 1
while True:
	if len(lotto) == 6:
		break
	r = random.randint(1, 6)
	chk = True
	# r값이 중복되는지 체크
	for j in range(len(lotto)):
		if lotto[j] == r:
			chk = False
			break
	if chk:
		lotto.append(r)
	i += 1

print(lotto)

# 정렬
tmp = 0
# 비교는 마지막인덱스-1 까지 가능
for idx in range(len(lotto) - 1):
	max = 0
	for i in range(idx, len(lotto)):
		if lotto[i] > max:
			max = lotto[i]
	for j in range(len(lotto)):
		if lotto[j] == max:
			tmp = lotto[idx]
			lotto[idx] = lotto[j]
			lotto[j] = tmp

print(lotto)

