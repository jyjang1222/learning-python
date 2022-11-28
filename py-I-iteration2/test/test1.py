"""
[문제]
    어떤사각형의 가로와 세로를 구하고싶다.
    다음 조건에 맞는 사각형 구하는 식을 적으시오.
    최소 길이는 1m 이며 , 1m단위로 계산한다. 
    [1] 사각형의 넓이는 24m이다.
    [2] 사각형의 가로는 세로보다 길다.
    [3] 사각형의 가로길이는 세로길이보다 2배는 넘는다. 
    [4] 사각형의 가로길이는 세로길이보다 3배는 넘지않는다.

"""
"""
[문제]
    중학생인 미연이는 부모님과 함께 미술관에 갔다.
    어른의 입장료가 청소년의 입장료보다 2,000원이 더 비싸고,
    세 사람의 입장료가 13,000원일때, 미연이의 입장료를 구하시오.
[정답]
    미연
"""
'''
	[문제]
		아래 배열은 3명의 학생 데이터이다.		
		각 학생은 3개씩 데이터로 표현한다. 
		맨 앞은 번호, 그다음은 국어점수, 그다음은 수학점수이다.					
		(예) 
			1001번, 국어 100, 수학 20
			1002번, 국어 32,  수학 54
			1003번  국어 34,  수학 65	

		
		[4] 전체 1등 학생을 출력하시오.
'''

a = [1001, 100, 20, 1002, 32, 54, 1003, 34, 65]





# 1
가로 = 1
세로 = 1
'''
가로 * 세로 = 24
가로 > 세로 * 2
가로 < 세로 * 3
'''


while True:
    i = 1
    while i <= 24:
        if i > 세로 * 2 and i < 세로 * 3 and i * 세로 == 24:
            print("가로:", i, "세로:", 세로)
            break
        i += 1
    if i * 세로 == 24:
        break
    세로 += 1


# 1정답
i = 1
while i <= 24:
    garo = i
    sero = 24 // i
    if 24 % i == 0 :
        if garo > sero and garo  > sero * 2 and garo  < sero * 3:
            print(garo , sero)

    i += 1
# ------------


# 2
미연 = 13000
어른 = 0
total = 13000

while True:
    if 미연 + (미연 + 2000) * 2 == total:
        print(미연)
        break
    미연 -= 100
    어른 += 100
# 3
a = [1001, 100, 20, 1002, 32, 54, 1003, 34, 65]
# 0 3 6
score = []
cnt = 0
sum = 0

for i in range(len(a)):
    if i % 3 == 0:
        continue
    sum += a[i]
    cnt += 1
    if cnt == 2:
        score.append(sum)
        sum = 0
        cnt = 0

print(score)
maxIdx = 0
max = 0

for i in range(len(score)):
    if max < score[i]:
        max = score[i]
        maxIdx = i

best = maxIdx * 3
print(maxIdx, a[best])



# 3정답
a = [1001, 100, 20, 1002, 32, 54, 1003, 34, 65]

i = 0
number = 0
kor = 0
math = 0
mx = 0
while i < len(a):
    total =  a[i + 1] +  a[i + 2]
    if total >= mx:
        mx = total
        kor = a[i + 1]
        math = a[i + 2]
        number = a[i]
    i += 3
print(number ,kor, math, mx)