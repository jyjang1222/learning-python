import random
'''
	[문제]
		복권 1개당 7칸으로, 총 5개의 복권을 제작하려 한다.
		복권 1줄은 1 또는 7의 랜덤 숫자로 구성되어 있다.
		7이 연속으로 3개 이상이면 "당첨"이고, 그 미만은 "꽝"이다.
		5개 중에 딱 1개만 당첨 복권이고 나머지 4개는 꽝인 복권을
		랜덤으로 생성해서 출력하시오.
		
		예)
			1177117 (꽝)
			1117771 (당첨)
			7171117 (꽝)
			7711771 (꽝)
			7171717 (꽝)
'''
lotto = []

win = 0
lose = 0

while len(lotto) < 5:
	# 로또생성
	tmp = []
	for j in range(7):
		r = random.randint(0, 1)
		if r == 0:
			r = 7
		tmp.append(r)
		
	# 당첨체크
	chk = False
	for j in range(len(tmp) - 2):
		cnt = 0
		for k in range(3):
			if tmp[j + k] == 7:
				cnt += 1
		if cnt == 3:
			chk = True
			break

	# 당첨이면
	if chk:
		# 당첨이 이미나왔으면 
		if win >= 1:
			continue
		lotto.append(tmp)
		win += 1
	# 꽝이면
	else:
		# 꽝이 이미 4개이면
		if lose >= 4:
			continue
		lotto.append(tmp)
		lose += 1
		
for i in range(len(lotto)):
	print(lotto[i])
