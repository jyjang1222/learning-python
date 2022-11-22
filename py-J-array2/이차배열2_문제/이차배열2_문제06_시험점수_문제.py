'''
    student리스트는 이번 학기 중간고사 성적이다.
    가로 한 줄을 기준으로 맨 앞은 번호이고, 뒤에 숫자 3개는
    각각 국어, 수학, 영어 점수이다. 
'''
student = [
    [1001, 100, 20, 32],        # 152
    [1002, 40, 43, 12],         # 95
    [1003, 60, 21, 42],         # 123
    [1004, 76, 54, 55],         # 185
    [1005, 23, 11, 76],         # 110
]
rank = []

'''
    [문제1] 
        모든 점수의 총합을 출력하시오.
    [정답1] 
        665
'''
print("[문제1]")

total = 0
for i in range(len(student)):
    for j in range(1, len(student[i])):
        total += student[i][j]
print(total)

'''
    [문제2] 
        국어 1등 번호를 출력하시오.
    [정답2]         	
        1001
'''
print("[문제2]")

korBest = 0
for i in range(len(student)):
    # 국어점수 [i][1], 학생번호 [i][0]
    if student[i][1] > korBest:
        korBest = student[i][1]
        idx = i

print(student[idx][0])

'''
    [문제3] 
        수학 1등 번호를 출력하시오.
    [정답3]    
        1004    
'''
print("[문제3]")

mathBest = 0
for i in range(len(student)):
    # 수학점수 [i][2], 학생번호 [i][0]
    if student[i][2] > mathBest:
        mathBest = student[i][2]
        idx = i

print(student[idx][0])

'''        	
    [문제4] 
        영어 1등 번호를 출력하시오.
    [정답4]
        1005
'''
print("[문제4]")

engBest = 0
for i in range(len(student)):
    # 수학점수 [i][2], 학생번호 [i][0]
    if student[i][3] > engBest:
        engBest = student[i][3]
        idx = i

print(student[idx][0])

'''
    [문제5] 
        전체 1등 번호를 출력하시오.
    [정답5]
        1004
'''
print("[문제5]")

bestScore = 0

for i in range(len(student)):
    sum = 0
    # 점수의 합
    for j in range(1, len(student[i])):
        sum += student[i][j]
    # 점수의합이 베스트점수 보다 크다면
    if sum > bestScore:
        bestScore = sum
        bestNum = i

print(student[bestNum][0])

'''
    [문제6] 
        수학점수가 국어점수 보다 높은 번호를 출력하시오.
    [정답6]
        1001 1003 1004 1005
'''
print("[문제6]")


for i in range(len(student)):
    # 수학점수 [i][2], 국어점수 [i][1]
    if student[i][2] > student[i][1]:
        idx = i
        print(student[idx][0])

'''
    [문제7]
        세 과목의 총합의 등수를 rank리스트에 저장하시오.
    [정답7]
        [2, 5, 3, 1, 4]
'''
print("[문제7]")

sumArr = []
for i in range(len(student)):
    sum = 0
    # 점수의 합
    for j in range(1, len(student[i])):
        sum += student[i][j]
    sumArr.append(sum)

print(sumArr)

for i in range(len(sumArr)):
    cnt = 1
    for j in range(len(sumArr)):
        if sumArr[j] > sumArr[i]:
            cnt += 1
    rank.append(cnt)

print(rank)





