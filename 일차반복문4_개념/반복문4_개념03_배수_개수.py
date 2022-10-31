'''
[문제] 
    100 이상인 7의 배수 중 
    3개만 차례대로 출력하시오.
[정답]
    105
    112
    119
[설명]
    배수는 범위를 특별히 제한하지 않으면 계속해서 커지기 때문에,
    위 문제를 풀기 위해선 무한 반복문을 사용해야 한다.
'''

# 풀이
i = 100
count = 0

while i >= 100:
    if i % 7 == 0:
        count += 1
        print(i)
        if count == 3:
            break
    i += 1


# i = 100
# count = 0

# run = 1
# while run == 1:
#     if i % 7 == 0:
#         print(i)
#         count += 1
#         if count == 3:
#             run = 0
#     i += 1









