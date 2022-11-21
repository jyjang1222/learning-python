'''		
	[문제]
        책이 총 78page이다. 
        [1] 철수는 책을 64page 읽었다. 몇 퍼센트 읽은 것인가?	
            소수점 두 자리까지 구하시오.		
        [2] 철수는 책을 30퍼센트 읽었다. 현재 페이지는 몇인가?		
    [정답]
        [1] 82.05
        [2] 30
'''
'''
    78페이지 : 100% = 64페이지 : n%
    78n = 100 x 64
    n = 100 x 64 / 78
'''

전체페이지_수 = 78

읽은페이지_수 = 64
읽은페이지_퍼센트 = 읽은페이지_수 * 100 / 전체페이지_수
print(round(읽은페이지_퍼센트, 2))

'''
    100% : 78페이지 = 30% : n페이지
    100n = 78 x 30
    n = 78 x 30 / 100
'''
읽은페이지_퍼센트 = 30
현재_페이지 = 전체페이지_수 * 읽은페이지_퍼센트 / 전체페이지_수
print(현재_페이지) 

