'''
    [문제]
        철수는 비밀번호는 아래와 같다. 
        철수는 비밀번호를 보호하기 위해 비밀번호 글자 사이사이에 
        알파벳을 a부터 순서대로 끼워넣었다.
        철수가 만든 비밀번호를 만들어보시오.
    [결과]
        qawbecrd1e2f3g4h
'''
password = "qwer1234"
sample = "abcdefghijklmnopqrstuvwxyz"



# 2
res = ''
for i in range(len(password)):
    res += password[i]
    if i == len(password) - 1:
        break
    res += sample[i]

print(res)

# 1
# tmp = ""

# for i in range(len(password)):
#     tmp += password[i]
#     tmp += sample[i]

# print(tmp)
