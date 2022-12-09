# from pickle import FALSE
'''
    # \n 은 줄바꿈이다.  구분자도 (\n 으로 넣으면 자르기할수있다.)

	[문제] 위 데이터 는  각각의 회원이 물건을 구입가격들 을 기록한 내용이다.
		회원별 구입 총합을 테이블로 만들려고한다.
		데이터는 아래와 같이 나올수있도록 함수를 만드시오.
		단, 스플릿함수는 직접구현하시오.
	[정답]
		{'number': '10001', 'name': '김철수', 'total': 2670}
		{'number': '10002', 'name': '이영희', 'total': 1950}
		{'number': '10003', 'name': '유재석', 'total': 4080}
		{'number': '10004', 'name': '박명수', 'total': 7130}
'''

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


data = ""
data += "10001/김철수/600\n"
data += "10002/이영희/800\n"
data += "10001/김철수/1400\n"
data += "10003/유재석/780\n"
data += "10002/이영희/950\n"
data += "10004/박명수/330\n"
data += "10001/김철수/670\n"
data += "10003/유재석/3300\n"
data += "10002/이영희/200\n"
data += "10004/박명수/6800\n"
data = data[0:-1] # 마지막글자  (\n)  삭제
#print(data)

tmp1 = mySplit('\n', data)
# print(tmp1)
tmp2 = []
for i in tmp1:
	tmp = mySplit('/', i)
	tmp2.append(tmp)
# print(tmp2)

def arrToDict(arr):
	tmp = []
	for i in arr:
		dict = {}
		for j in range(len(i)):
			dict['number'] = int(i[0])
			dict['name'] = i[1]
			dict['total'] = int(i[2])
		tmp.append(dict)
	return tmp

dataDict = arrToDict(tmp2)

# for i in dataDict:
# 	print(i)

# 중복데이터 합치기
def combineDuplicatedData(dict):
	tmp = []
	for i in dict:
		chk = True
		for j in tmp:
			if i['number'] == j['number']:
				chk = False
				j['total'] += i['total']
		if chk:
			tmp.append(i)
	return tmp

totalDict = combineDuplicatedData(dataDict)

for i in totalDict:
	print(i)









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

# def getSplit(data):
# 	arr = []
# 	token1 = mySplit(data , "\n")
# 	#print(token1)
# 	for i in range(len(token1)):
# 		token2 = mySplit(token1[i] , "/")
# 		arr.append(token2)
# 	return arr

# def getTotal(dataList):
# 	# print(dataList)
# 	memberList = []
# 	for i in range(len(dataList)):
# 		check = False
# 		for j in range(len(memberList)):
# 			if memberList[j]["number"] == dataList[i][0]:
# 				check = True
# 				break
# 		if check == False:
# 			temp = {"number" : dataList[i][0] ,"name" : dataList[i][1] ,  "total" : 0}
# 			memberList.append(temp)

# 	for i in range(len(memberList)):
# 		for j in range(len(dataList)):
# 			if memberList[i]["number"] == dataList[j][0]:
# 				memberList[i]["total"] += int(dataList[j][2])

# 	return memberList


# def quiz1(data):
# 	dataList = getSplit(data)
# 	# print(dataList)
# 	totalList = getTotal(dataList)
# 	for i in range(len(totalList)):
# 		print(totalList[i])
# quiz1(data)