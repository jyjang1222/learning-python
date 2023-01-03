'''
[문제] 
    280의 약수 중에
    50바로 전의 값과 바로 뒤의 값을 구하시오.
    만약 50이 약수이면, 바로 뒤의 값은 50이다.
[정답]
    40
    56
'''

# 풀이 (푸는데 시간 좀 걸렸음)

# num = 0
# num2 = 0
# i = 1

# while i <= 280:
#     if i < 50 and 280 % i == 0:
#         num = i
#     if i > 50 and 280 % i == 0:
#         num2 = i
#         break
#     i += 1
    
# print(num, num2)
# 정답
# front = 0
# back = 0

# i = 1
# while i <= 280:
#     if 280 % i == 0:
#         if i < 50:
#             front = i
#         if i >= 50 and back == 0:
#             back = i
#     i += 1

# print(front)
# print(back)


# 2트
'''
[문제] 
    280의 약수 중에
    50바로 전의 값과 바로 뒤의 값을 구하시오.
    만약 50이 약수이면, 바로 뒤의 값은 50이다.
[정답]
    40
    56
'''

n = 280
ans = 0
for i in range(1, n+1):
    if n % i == 0:
        if i < 50:
            ans = i
        if i > 50:
            print(ans)
            ans = i
            print(ans)
            break

n = 280
arr = []
for i in range(1, n+1):
    if n % i == 0:
        arr.append(i)

for i in range(len(arr)):
    if arr[i] > 50:
        print(arr[i-1])
        print(arr[i])
        break