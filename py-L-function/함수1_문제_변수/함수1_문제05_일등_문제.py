'''
    [문제]
        아래 리스트는 시험 점수와 학생 이름이다.
        일등의 학생 이름을 출력해주는 함수를 만드시오.
    [정답]
        1등 학생 = 박민지
'''

name = ["이만수", "김철수", "박민지"]  
score = [54, 32, 92]

def printBestStudent(nameArr, scoreArr):
    rankArr = []
    for i in score:
        rank = 1
        for j in score:
            if i < j:
                rank += 1
        rankArr.append(rank)
    for i in range(len(rankArr)):
        if rankArr[i] == 1:
            print(score[i], name[i])

printBestStudent(name, score)