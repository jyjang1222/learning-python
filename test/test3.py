"""
    [문제] 9와 0 이 없는 세상 

        숫자 1부터 1씩 증가하며 순서대로 20번 출력한다. 
        단 9와 0이 없다. 
    [예시]
        1 2 3 4 5 6 7 8 11 12 13 14 15 16 17 18 21 22 23 24
"""
print("--[문제1]--")

# 1
# count = 0

# for i in range(1000):
#     if i % 10 == 9 or i % 10 == 0:
#         continue
#     if i >= 10:
#         if i // 10 == 9:
#             continue
#     if count == 99:
#         break
#     print(i, end = " ")
#     count +=1

# print()
# 2
count = 0
i = 0
while True:
    if count == 99:
        break
    i += 1
    if i % 10 == 9 or i % 10 == 0:
        continue
    if i % 100 // 10 == 0:
        continue
    if i >= 10:
        if i // 10 == 9:
            continue
    print(i, end = " ")
    count += 1

print(count)