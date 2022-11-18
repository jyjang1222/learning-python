import random
"""
    [면접문제1]
        a에 랜덤숫자 (1~100) 사이의 값 20개를 저장하고 다음 조건대로 모두 출력하시오.

        [1] 최소값 [2] 최대값  [3] 합계 [4] 평균 [5] 중간값 
"""

print("#1")

a = []
min = 100
max = 0
sum = 0
avg = 0

for i in range(20):
    r = random.randint(1, 100)
    a.append(r)

for i in a:
    if min > i:
        min = i
    if max < i:
        max = i
    sum += i
avg = round(sum / len(a), 2)

print(min, max, sum, avg)

for i in a:
    if i != min and i != max:
        print(i, end = " ")


print("#2")

"""
    [면접문제2]
        b 에 랜덤 숫자 (0~9)사이의 값을 5개 저장하고 그래프로 표현하시오.

    [예시]
        b = [5,6,3,0,9]
    [출력]
        5*****
        6******
        3***
        0
        9*********
"""



b = []
for i in range(5):
    r = random.randint(0, 9)
    b.append(r)

print(b)

for i in range(len(b)):
    # j = b[i]
    print(b[i], end = "")
    for j in range(b[i]):
        print("*", end = "")
    print()


print("#3")
"""
    [면접문제3]
        랜덤으로 숫자 (1~5) 을 10번 출력하고 각각 몇번씩 나왔는지 출력하시오.
    [예시]
        c = [1,4,4,5,4,3,3,1,2,2]
    [결과]
        1 : 2번
        2 : 2번
        3 : 2번
        4 : 3번
        5 : 1번 
"""
c = []

for i in range(10):
    r = random.randint(1, 5)
    c.append(r)

print(c)


for i in range(1, 6):
    cnt = 0
    for j in range(len(c)):
        if i == c[j]:
            cnt += 1
    print(i, ":", cnt)



print("#4")
"""
    [면접문제4]
        숫자 1과 2는 한쌍이며, 순서는 1다음에 2가 바로있어야한다.  
        다음 리스트에서 1과2가 붙어있는걸 한번이라고했을때 몇번 반복되는지 출력하시오.
    [예시1]
        [3,1,2,1,2,5] => 2번
    [예시2]
        [1,1,2,4,3,4] => 1번 
"""
test1 = [3,1,2,1,2,5]
test2 = [1,1,2,4,3,4]

prev = 0
cnt = 0

for i in range(len(test1)):
    if prev == 1:
        if test1[i] == 2:
            cnt += 1
    prev = test1[i]
    
print("test1", cnt)

cnt = 0

for i in range(len(test2)):
    if prev == 1:
        if test2[i] == 2:
            cnt += 1
    prev = test2[i]

print("test2", cnt)