import random
'''
	[문제]
		[1] 랜덤숫자 1~9 다섯 개를 리스트에 추가한다.
		[2] 그 숫자 중 홀수만 하나로 모아서 숫자로 만든다. (더하기가 아니다.)
		[3] 그 숫자의 두 배를 출력한다. 
	
	[예시] 
		2 5 3 4 6 이 랜덤으로 저장되었다고 가정했을 때,
		홀수는 5, 3 이므로 합치면 53이 된다. 
		53의 두 배는 106이다. 
'''

a = []
# temp = []
num = 0


for i in range(5):
	r = random.randint(1, 9)
	a.append(r)

j = 1
i = len(a) - 1
while i >= 0:
	if a[i] % 2 == 1:
		num += a[i] * j
		j *= 10
	i -= 1

print(a)
print(num * 2)