'''
	[문제]
	 	철수는 자전거를 타고 일정한 빠르기로 2시간 동안 37876m를 갔다.
	 	철수가 자전거를 타고 30초 동안 간 거리를 구하시오.
	 	소수점 두 자리까지 구하시오. 
	 	
	[정답] 
		157.82
'''

이동_시간 = 2 * 3600
이동_거리 = 37876

삼십초_이동거리 = 이동_거리 / 이동_시간 * 30
print(round(삼십초_이동거리, 2))