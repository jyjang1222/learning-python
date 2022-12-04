'''
    [문제]
        1. 1~100까지 반복한다.
        2. 각 수에 3이나 6이나 9의 개수를 누적해서 출력하시오. 

        [예시]
            3 1
            6 1
            9 1
            13 1
            16 1
            ...
            98 1
            99 2
'''

i = 1
count = 0

while i < 100:
    count = 0
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        count += 1
    if i // 10 == 3 or i // 10 == 6 or i // 10 == 9:
        count += 1
    print(i, count)
    i += 1

# 1000까지 369갯수세기
count = 0
for i in range(1, 1001):
    j = i
    while j != 0:
        if j % 10 == 3 or j % 10 == 6 or j % 10 == 9:
            count += 1
        j //= 10
print(count)    