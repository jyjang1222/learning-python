'''
    [문제]
        철수는 a리스트에서 숫자 검사를 해야한다.
        각 단어를 검사해서 해당 메시지 중 하나를 출력하시오.
    [정답]
        문자만 있다
        숫자만 있다
        문자와 숫자가 섞여있다.
'''
a = ["adklajsiod", "123123", "dasd12312asd"]
msg = ["문자만 있다", "숫자만 있다", "문자와 숫자가 섞여있다."]

num = '0123456789'
str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(a)):
    chkNum = False
    chkStr = False
    for j in range(len(a[i])):

        for k in range(len(num)):
            if a[i][j] == num[k]:
                chkNum = True
        for k in range(len(str)):
            if a[i][j] == str[k]:
                chkStr = True
    if chkNum and chkStr == False:
        print(a[i], msg[1])
    elif chkNum == False and chkStr:
        print(a[i], msg[0])
    elif chkNum and chkStr:
        print(a[i], msg[2])