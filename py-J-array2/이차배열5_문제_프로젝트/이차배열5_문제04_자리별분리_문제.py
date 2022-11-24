import random
'''
	[문제]
		랜덤으로 10000 ~ 99999 사이의 랜덤숫자를 저장하고 
		다음 규칙에 따라 결과를 출력하시오.
		랜덤숫자를 두 개로 분리하는데
		한 자리씩 늘리면서 분리한다. 
		각 분리한 숫자의 합을 출력한다.
	[예시]
		r = 34567
	[결과]
		3 + 4567
		34 + 567
		345 + 67
		3456 + 7
'''

r = random.randint(10000, 99999)
# r = 34567
print(r)
cnt = 0
tmp = r
while True:
	if tmp // 10 == 0:
		break
	tmp //= 10
	cnt += 1

print(cnt)
print()

n1 = 0
n2 = 0
# 1
for i in range(cnt, 0, -1):
	n1 = r // (10 ** i)
	n2 = r % (10 ** i)
	print(n1 + n2)

# 2
i = 1
for j in range(cnt):
	i *= 10
while i > 1:
	n1 = r // i
	n2 = r % i
	print(n1 + n2)
	i //= 10