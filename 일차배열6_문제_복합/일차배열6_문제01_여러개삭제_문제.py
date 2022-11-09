import random
'''
    [문제]  
        아래 a리스트는 순서대로 값이 저장되어있다.
        랜덤(1~100)숫자 하나를 저장 후,
        랜덤 값보다 작은 값은 전부 a리스트에서 삭제하시오.
    [정답]

'''

a = [10, 20, 30, 40, 50, 60]

r = random.randint(1, 100)
print(r)

# 풀다헤맴
# for i in a:
#     print(i)
#     if i < r:
#         a.remove(i)
#         print(a)

# 1차풀이
# i = len(a) - 1
# while i >= 0:
#     if a[i] < r:
#         a.remove(a[i])
#         print(a)
#     i -= 1

# 2
b = [10, 20, 30, 40, 50, 60]

for i in b:
    if i < r:
        a.remove(i)
        print(a)