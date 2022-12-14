'''
[문제]
    1. 1~50까지 반복한다.
    2. 그 안에서 해당 숫자의 369게임의 결과를 출력한다.
    3. 각각의 숫자에 3이나 6이나 9가 두 개면 "짝짝"
    4. 각각의 숫자에 3이나 6이나 9가 한 개면 "짝"
    5. 3이나 6이나 9가 없으면 그냥 숫자를 출력하시오.
    
[결과] 
    1 2 짝 4 5 짝 7 8 짝 10 11 12 짝 ...
'''

# i = 1
# 박수 = ""

# while i <= 50:
#     박수 = ""
#     # 기존코드
#     if not(i % 10 == 3 or i % 10 == 6 or i % 10 == 9):
#         if not(i // 10 == 3 or i // 10 == 6 or i // 10 == 9):
#             print(i, end = "")
#     # ----------------------
#     if i // 10 == 3 or i // 10 == 6 or i // 10 == 9:
#         박수 += "짝"
#     if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
#         박수 += "짝"
#     # 정답을 본후 코드개선사항
#     if 박수 == "":
#         print(i, end = "")
#     # -----------------------
#     print(박수)
#     i += 1


# i = 1
# while i <= 50:
#     십의자리 = i // 10
#     일의자리 = i % 10

#     count = 0
#     if 십의자리 == 3 or 십의자리 == 6 or 십의자리 == 9:
#         count += 1
#     if 일의자리 == 3 or 일의자리 == 6 or 일의자리 == 9:
#         count += 1  

#     if count == 2:
#         print("짝짝")  
#     if count == 1:
#         print("짝")
#     if count == 0:
#         print(i)
        
#     i += 1

# 2트
'''
[문제]
    1. 1~50까지 반복한다.
    2. 그 안에서 해당 숫자의 369게임의 결과를 출력한다.
    3. 각각의 숫자에 3이나 6이나 9가 두 개면 "짝짝"
    4. 각각의 숫자에 3이나 6이나 9가 한 개면 "짝"
    5. 3이나 6이나 9가 없으면 그냥 숫자를 출력하시오.
    
[결과] 
    1 2 짝 4 5 짝 7 8 짝 10 11 12 짝 ...
'''

arr369 = [3,6,9]
for n in range(1, 51):
    current = n
    박수 = ''
    while current != 0:
        if current % 10 in arr369:
            박수 += '짝'
        current //= 10
    print(n, 박수, end=" ")







