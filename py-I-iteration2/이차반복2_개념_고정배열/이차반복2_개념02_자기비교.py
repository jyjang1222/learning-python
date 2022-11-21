'''
	[문제]
		a리스트는 철수 반 중간고사 점수이다. 
		각 학생들이 다른 학생들과 비교하여 자기보다 크거나 같은 점수를 출력하시오.
	[예시]
		10 보다 큰 점수는 54, 90, 20 이다.
		54 보다 큰 점수는 90 이다.
		90 보다 큰 점수는 없다.
		20 보다 큰 점수는 54, 90 이다. 
'''

a = [10, 54, 90, 20, 54]
# cnt = 0
for i in range(len(a)):
	print(a[i], "보다 크거나 같은 점수는")
	cnt = 0
	for j in range(len(a)):
		# 본인인덱스 제외
		if i == j:
			j += 1
			continue
		# 같거나 큰점수 출력
		if a[i] == a[j] or a[i] <= a[j]: 
			cnt += 1
			print(a[j], end = " ")
	if cnt == 0:
		print("없다")
	else:
		print("이다.")

print()
# 정답
for i in range(len(a)):
	for j in range(len(a)):
		if i != j and a[i] <= a[j]: # 본인 인덱스는 제외해야 한다.
			print(a[j] , end=" ")
	print()