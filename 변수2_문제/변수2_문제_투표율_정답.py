'''
	[문제]
 		철수네 반은 학생이 40명이다.
 	 	철수, 영희, 민수 이렇게 세 학생은 반장선거에 출마했다.
 	 	민수는 득표를 전체 중 40%를 획득했고, 
 	 	영희는 9표를 획득했다.
 	 	나머지는 철수가 득표했다.
 	 	철수의 전체 득표는 몇 퍼센트 인지 구하시오. 	
 	 	
    [정답] 
        37.50
'''
'''
    40명 : 100% = 9명 : n%
    40n = 100 x 9
    n = 100 x 9 / 40
'''

전체학생_수 = 40

민수_득표_퍼센트 = 40

영희_득표_수 = 9
영희_득표_퍼센트 = 영희_득표_수 * 100 / 전체학생_수

철수_득표_퍼센트 = 100 - 민수_득표_퍼센트 - 영희_득표_퍼센트
print(철수_득표_퍼센트)
