
"""
  [문제]
    아래  userData는 회원번호와이름이고 , 
    pointData는 포인트와 회원번호이다.
    포인트는 여러번쌓을수있고, 전부 누적해서 합을 구한다.
    포인터 점수가 가장높은 회원의 이름과 번호를 리스트로반환하는 함수를 만드시오.
    단, 직접만든 스플릿함수를 사용하시오.
  [정답]
    이만수  1002
      
"""

userData = "1001/김철수,"
userData += "1002/이만수,"
userData += "1003/이영희"

pointData = "1/1001,"
pointData += "1/1002,"
pointData += "2/1003,"
pointData += "1/1001,"
pointData += "2/1002"

print(userData, pointData)


def mySplit(str, data):
    i = 0
    arr = []
    tmp = ''
    while i < len(data):
        cnt = 0
        # 입력된 str과 같은지 체크
        if data[i] == str[0]:
            for j in range(len(str)):
                # 예외처리
                if i + j >= len(data):
                    break
                if data[i+j] == str[j]:
                    cnt += 1
        # 같으면
        if cnt == len(str):
            arr.append(tmp)
            tmp = ''
            i += len(str) # len(str)만큼 건너뜀
        else:
            tmp += data[i]
            i += 1

    arr.append(tmp)
        
    return arr

test1 = "1001,1002,1003,1004"
test2 = "1001,,1002,,1003,,1004"
test3 = "1001-,-1002-1003-,-1004-"
arr1 = mySplit(',', test1)
arr2 = mySplit(',,', test2)
arr3 = mySplit('-,-', test3)
print(arr1)
print(arr2)
print(arr3)

# mySplit으로 배열로 만들기
userTmp = mySplit(',', userData)
pointTmp = mySplit(',', pointData)

userArr = []
pointArr = []

for i in userTmp:
    tmp = mySplit('/', i)
    userArr.append(tmp)
for i in pointTmp:
    tmp = mySplit('/', i)
    pointArr.append(tmp)
    
print(userArr)
print(pointArr)

# 만들어진 배열 딕셔너리로 만들기
userDictArr = []
pointDictArr = []

for i in range(len(pointArr)):
    dict = {}

    memberNumber = pointArr[i][1]
    point = pointArr[i][0]

    dict['memberNumber'] = int(memberNumber)
    dict['point'] = int(point)

    pointDictArr.append(dict)

for i in range(len(userArr)):
    dict = {}

    memberNumber = userArr[i][0]
    name = userArr[i][1]

    dict['memberNumber'] = int(memberNumber)
    dict['name'] = name

    userDictArr.append(dict)

for i in pointDictArr:
    print(i)
for i in userDictArr:
    print(i)

# pointDictArr 누적시키기
tmp = []

for i in range(len(pointDictArr)):
    chk = True
    for j in range(len(tmp)):
        # 중복체크
        if pointDictArr[i]['memberNumber'] == tmp[j]['memberNumber']:
            chk = False
            # 중복이 있으니 누적
            tmp[j]['point'] += pointDictArr[i]['point']
    if chk:
        tmp.append(pointDictArr[i])

pointDictArr = tmp

for i in pointDictArr:
    print(i)

for i in range(len(pointDictArr)):
    rank = 1
    for j in range(len(pointDictArr)):
        if pointDictArr[i]['point'] < pointDictArr[j]['point']:
            rank += 1
    pointDictArr[i]['rank'] = rank

for i in pointDictArr:
    print(i)

bestMember = []
for i in range(len(pointDictArr)):
    if pointDictArr[i]['rank'] == 1:
        bestMember.append(userDictArr[i]['name'])
        bestMember.append(pointDictArr[i]['memberNumber'])

print(bestMember)











# 정답
# def mySplit(str, d):
# 	arr = []
# 	temp = ""
# 	for i in range(len(str)):
# 		if str[i] == d :
# 			arr.append(temp)
# 			temp = ""
# 		else:
# 			temp += str[i]
# 	arr.append(temp)
# 	return arr

# def getMax(userList , pointList):
#   maxPoint = 0
#   for i in range(len(userList)): 
#     user = userList[i]
#     total = 0
#   for j in range(len(pointList)):
#     point = pointList[j]
#     if user[0] == point[1]:
#       total += int(point[0])
#     if total > maxPoint:
#       maxPoint = total 
#   return user

# def maxPoint(userData , pointData):
#   userList = []
#   token1 = mySplit(userData , ",")
#   for i in range(len(token1)):
#     token2 = mySplit(token1[i] , "/")
#     userList.append(token2)

#   pointList = []
#   token1 = mySplit(pointData , ",")
#   for i in range(len(token1)):
#     token2 = mySplit(token1[i] , "/")
#     pointList.append(token2)

#   maxUser = getMax(userList, pointList)
#   print(maxUser)  
#print(userData)
#print(pointData)
# maxPoint(userData , pointData)




