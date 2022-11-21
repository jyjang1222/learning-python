'''
    [문제]
        아래 배열은 철수와 민수의 가위바위보 데이터이다. 
        왼쪽이 철수의 데이터이고 오른쪽이 민수의 데이터이다.
        가위(0), 바위(1), 보(2) 는 숫자로 표기한다.
        철수와 민수는 계단 가장 밑에서 게임을 시작했으며, 
        아래의 규칙을 따른다.

        [규칙]
            이기면 계단 3증가
            비기면 계단 1증가
            지면 계단 3감소 

            단, 지더라도 계단은 0미만으로 내려갈 수 없다.
        
        철수는 게임이 종료 후 몇 번째 계단에 있는지 구하시오.
    [정답]
        졌다! 0
        졌다! 0  
        졌다! 0  
        비겼다! 1
        비겼다! 2
        이겼다! 5
        
        철수의 위치 = 5   
'''
game = [
    [1,2],
    [1,2],
    [2,0],
    [0,0],
    [1,1],
    [2,1]
]
pos = 0
