'''
	[문제] 
		내 연봉에서 세금 10%를 제외했더니 1350만원이다.
		세금을 제외하기 전 내 월급은 얼마인지 구하시오.
		
	[정답] 
		125
'''

'''
    90% : 1350원 = 10% : n원
    90n = 1350 x 10
    n = 1350 x 10 / 90

'''

세후연봉 = 1350
세금_퍼센트 = 10

세금 = 세후연봉 * 세금_퍼센트 / (100 - 세금_퍼센트)

세전연봉 = 세후연봉 + 세금
세전월급 = 세전연봉 / 12
print(세전월급)
