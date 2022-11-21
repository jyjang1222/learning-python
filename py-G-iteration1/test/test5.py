import random

'''
    [문제]
        랜덤으로 3~8의 숫자를 저장한다. 
        랜덤숫자 3 이면 세자리 자리수를 뜻한다. 
        랜덤숫자 4 이면 네자리 자리수를뜻한다.
        랜덤숫자 8 이면 여덟자리 자리수를 뜻한다. 
        세자리수라면 100~999 사이의 랜덤숫자를 다시 출력
        네자리수라면 1000~9999 사이의 랜덤숫자를 다시 출력
        다섯자리수라면 10000~99999 사이의 랜덤숫자를 다시 출력
        ...
        여덟자리수라면 10000000~99999999 사이의 랜덤숫자를 다시 출력
    [주의]
        반복문을 사용할것  
    [예시] 
        r = 3  ==> 세자리수 534 
        r = 4  ==> 두자리수 1945 
        r = 5  ==> 다섯자리수 13534 
        ...
        r = 8  ==> 여덟자리수 56430145
'''
print("--[문제1]--")

# 1
r = random.randint(3, 8)
print(r)

# r2 = random.randint(10^r, 10^(r+1) - 1)

# 1.1
i = 1
j = 1
while True:
    if i == r:
        break
    j *= 10
    i += 1

# 1.2
# j = 1
# for i in range(r - 1):
#     j *= 10

r2 = random.randint(j, j * 10 - 1)

print(j, j * 10 - 1, r2)



# 정답
# print("--[문제1]--")
# import random
# r = random.randint(3, 8)
# i = 1
# a = 1
# print(r)
# while i < r:
#     a *= 10
#     i += 1
# b = a * 10 - 1
# print(a , " " , b)
# r  = random.randint(a , b)
# print(r)