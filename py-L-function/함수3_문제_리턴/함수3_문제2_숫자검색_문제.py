"""
    [문제]
        아래 stringTest 검사해서 숫자만 있는 값을  찾아서 리스트로 반환하는  함수를 만드시오.
    [정답]
        ['1234', '45345']
"""



stringList = ["qwer1234dasd" , "dasdasd" , "1234" , "45345" , "12das23"]

str = 'abcdefghijklmnopqrstuvwxyz'

def stringTest(arr):
    tmp = []
    for i in stringList:
        chk = True
        # 숫자만있는지 체크
        for j in i:
            for k in str:
                if j == k:
                    chk = False
        if chk:
            tmp.append(i)
    return tmp

res = stringTest(stringList)
print(res)















# 정답
# def getNumber(string):
#     sample = "0123456789"
#     count = 0
#     for j in range(len(string)):
#         for k in range(len(sample)):
#             if string[j] == sample[k]:
#                 count += 1
#                 break
#     if count == len(string):
#         return True
#     return False

# def checkNumber(stringList):
#     arr = []
#     for i in range(len(stringList)):
#         string = stringList[i]
#         if getNumber(string) == True:
#             arr.append(string)
#     return arr
# arr = checkNumber(stringList)
# print(arr)