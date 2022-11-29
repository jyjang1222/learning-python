'''
    [문제]
        철수는 비밀번호는 아래와 같다. 
        철수는 비밀번호를 보호하기 위해 비밀번호 글자 사이사이에 
        알파벳을 a부터 순서대로 끼워 넣었다.
        이제 철수는 원래 비밀번호로 다시 변환해야 한다.
        암호화된 비밀번호를 원래대로 복구하시오.
    [정답]
        qwer1234
'''
pw = "qawbecrd1e2f3g4h"


# 4
origin = ''

for i in range(0, len(pw), 2):
    origin += pw[i]

print(origin)


# 1 틀림
# c = 'a'
# tmp = int(c)
# for i in range(len(pw)):
#     if i % 2 == 1:
#         if int(pw[i]) == int(tmp):
#             pw = pw.replace(pw[i], '')
#     tmp += 1

# 2 틀림
# idx홀수제거
# i = 0
# while i < len(pw):
#     if i % 2 == 1:
#         pw.replace(pw[i], '')
#         print(pw)
#         # i -= 1
#     i += 1
# print(pw)

# 3 맞춤
# tmp에 짝수만 넣기
# tmp = ""
# for i in range(len(pw)):
#     if i % 2 == 0:
#         tmp += pw[i]

# print(tmp)
