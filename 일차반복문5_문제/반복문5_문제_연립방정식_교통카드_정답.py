'''
	[문제]
		선호네 반 학생 25명이 체험학습을 가기 위해
		버스를 탔는데, 총 요금이 19400원이었다.

		교통카드를 사용하면 720원이고, 
		현금으로 지불하면 1000원일 때, 

		교통카드를 사용한 학생 수와 현금을 사용한 학생 수는 
		각각 얼마인지 구하시오.
	[정답]
		카드 = 20
		현금 = 5
'''

총학생 = 25
총요금 = 19400

버스_카드_요금 = 720
버스_현금_요금 = 1000

카드_이용자수 = 총학생
현금_이용자수 = 0

run = 1
while run == 1:
	if 카드_이용자수 + 현금_이용자수 == 총학생 and 버스_카드_요금 * 카드_이용자수 + 버스_현금_요금 * 현금_이용자수 == 총요금:
		print("카드 =", 카드_이용자수)
		print("현금 =", 현금_이용자수)
		run = 0
	else:
		카드_이용자수 -= 1
		현금_이용자수 += 1
