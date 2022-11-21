'''
	[문제]
		아래 a리스트의 값을 자리별로 분리 후,
		그 합을 total 리스트에 추가하시오.
	[예시]
		[1] 1 + 3 + 2  				total = [6]
		[2] 4 + 3 + 5 + 4  			total = [6,16]
		[3] 2 + 3 + 3 				total = [6,16,8]
		[4] 6 + 6 + 7 + 6 + 5  		total = [6,16,8,30]
	[정답]
		total = [6, 16, 8, 30]
'''

a = [132, 4354, 233, 66765]
total = []

# 방법1
for i in a:
	size = 0
	j = 10
	while True:
		if i // j != 0:
			size += 1
		if i // j == 0:
			break
		j *= 10

	sum = 0
	cnt = 0
	k = 1
	# sum += i // 100
	sum += i // (10 ** size)
	while cnt < size:
		# sum += i % 100 // 10
		# sum += i % 10 // 1
		sum += i % (10 * k) // k
		k *= 10
		cnt += 1

	total.append(sum)

print(total)

# 방법2 (정답보고 다시푼 풀이)
total = []

for i in a:
	tmp = i

	sum = 0
	while True:
		sum += tmp % 10
		tmp //= 10
		if tmp == 0:
			break

	total.append(sum)

print(total)