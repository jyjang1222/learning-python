'''
    [문제]
        아래 dbId와 logId가 서로 일치하는지 검사하시오.
        단, 대소문자를 구분하지 않는다. 
        즉, A나 a나 서로 같은 것이다.
    [정답]
'''		
dbId = "q1W2E3r4"
logId = "q1w2e3R4"

str1 = 'abcdefghijkmlnopqrstuvwxyz'
str2 = 'ABCDEFGHIJKMLNOPQRSTUVWXYZ'

for i in range(len(dbId)):
    for j in range(len(str1)):
        if dbId[i] == str1[j]:
            dbId = dbId.replace(dbId[i], str2[j])
        if logId[i] == str1[j]:
            logId = logId.replace(logId[i], str2[j])

print(dbId, logId)
if dbId == logId:
    print(True)


















#힌트
str0 = "0123456789"
str1 = "abcdefghijklmnopqrstuvwxyz"
str2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

