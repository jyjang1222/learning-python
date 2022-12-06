'''
   [문제]
        text는 학생점수를 기록한 데이터이다.
        전체 평균과 일등의 점수를 출력하시오.
    [정답]
        평균 = 30.2
        일등 점수 = 80
'''
text = "13,32,80,3,23"

strArr = text.split(',')
intArr = []

sum = 0
best = 0
for i in strArr:
    sum += int(i)
    if int(i) > best:
        best = int(i)
    intArr.append(int(i))

avg = round(sum / len(strArr), 2)

print(avg, best)
print(strArr)
print(intArr)