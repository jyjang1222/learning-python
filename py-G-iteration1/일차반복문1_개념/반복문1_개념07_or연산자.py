'''
[문제] 
    [조건1] 1~20 사이의 숫자를 출력한다. 
    [조건2] 5 이하이거나 15 이상은 숫자 대신 "aa"를 출력하시오.
[정답]
    aa
    aa
    aa
    aa
    aa
    6
    7
    8
    9
    10
    11
    12
    13
    14
    aa
    aa
    aa
    aa
    aa
    aa
'''
# 풀이
i = 1
while i <= 20:
    if not(5 < i and i < 15):
        print("aa")
        i += 1
        continue
    print(i)
    i += 1






# i = 1
# while i <= 20:
#     # 5이하 이거나 15이상일 때
#     if 15 <= i or i <= 5:
#         print("aa")
#     # 5초과 그리고 15미만일 때
#     if 5 < i and i < 15:
#         print(i)
#     i += 1
