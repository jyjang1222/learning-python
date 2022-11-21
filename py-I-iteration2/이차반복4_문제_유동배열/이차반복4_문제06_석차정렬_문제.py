'''
	[문제]
		석차를 출력하시오.
	[정답]
		2 3 4 1 
'''

numList = [1001, 1002, 1003, 1004]
scoreList = [87, 42, 11, 98]
rank = [0, 0, 0, 0]
prevMax = 100

for i in range(len(scoreList)):
	max = 0
	maxIdx = 0
	for j in range(len(scoreList)):
		# 이전최대값보다 작은수만 비교
		if scoreList[j] < prevMax:
			if max < scoreList[j]:
				max = scoreList[j]
				maxIdx = j
	# 이전최대값 저장
	prevMax = max
	print(prevMax)
	# 순위저장
	rank[maxIdx] = i + 1
	print(rank)
