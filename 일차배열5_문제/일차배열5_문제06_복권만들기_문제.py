import random
'''
	[문제] 
		a리스트 안에 1 또는 7을 랜덤으로 7개 추가 후 출력하시오. 
		단, 7의 개수는 3개만 추가하고, 1의 개수는 4개만 추가한다.
		위에서 만든 복권을 판정한다. 
  		7이 연속으로 3개면 "당첨"을 출력한다.
		아니면 "꽝"을 출력한다.
		
	[예]
		[ 1, 7, 7, 1, 1, 7, 1]  "꽝"
		[ 1, 1, 1, 7, 7, 7, 1]  "당첨"
'''

lotto = []
count1 = 0
count7 = 0
res = True

while True:
	if len(lotto) == 7:
		break
	r = random.randint(0, 1)
	if r == 0:
		if count7 == 3:
			continue
		lotto.append(7)
		count7 += 1
	if r == 1:
		if count1 == 4:
			continue
		lotto.append(r)
		count1 += 1

for i in range(1, len(lotto)):
	count = 0
	if lotto[i] == 7:
		count += 1
		if count >= 1:
			if lotto[i - 1] != lotto[i]:
				res = False
				
print(lotto, res)
	
