'''
	[문제]    
		철수는 3만 원을 가지고 친구 3명 포함 총 4명이, 
		돈가스를 각각 1개씩 사 먹었더니 남은 돈이 2000원이었다. 	
	
		위 식을 표현하고, 풀이 과정을 주석으로 작성하시오.
    [정답]
		7000
'''
'''
    돈가스 총 가격 = 현금30000 - 잔돈2000 = 28000

    돈가스 1개 가격 = 28000 / 4 = 7000
'''

현금 = 30000
잔돈 = 2000
총인원 = 4

돈가스_가격 = (현금 - 잔돈) / 4
print(돈가스_가격)