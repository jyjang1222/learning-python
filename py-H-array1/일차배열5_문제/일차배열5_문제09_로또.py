import random
'''
	[로또]	
		아래 lotto 리스트에 1~45숫자를 순차적으로 저장한다. 
		셔플후 그중 가장앞에서 6개를 출력한다. 
'''
lotto = []

for i in range(1, 46):
	lotto.append(i)

print(lotto)

tmp = 0

while i <= 1000:
	for j in range(len(lotto)):
		r = random.randint(0, 44)

		tmp = lotto[r]
		lotto[r] = lotto[j]
		lotto[j] = tmp

	i += 1

print(lotto)

for i in range(6):
	print(lotto[i], end = " ")


