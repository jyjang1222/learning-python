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
총학생 = 40
민수 = 40 * 40 / 100
영희 = 9
철수 = 총학생 - 민수 - 영희

print(철수 / 총학생 * 100)