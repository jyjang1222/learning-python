'''
	[문제] 
		200의 약수 중에서 짝수 중 
		80에 가장 가까운 수를 구하시오.
		만약 약수 중에 80이 있을 경우, 80이 정답이다.
	[정답]
		100
'''

i = 2
prev = 0
next = 0

while i <= 200:
	if i <= 80 and 200 % i == 0:
		prev = i
	if i > 80 and 200 % i == 0:
		next = i
		break
	i += 2

if next - 80 > 80 - prev:
	print(prev)
else:
	print(next)