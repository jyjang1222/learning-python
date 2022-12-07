'''
	[문제]
		rentalList는 도서관 책 대여 데이터이다.
		memberList는 책을 대여해간 회원 데이터이다. 
		오늘은 2020년12월4일 이다.
		책을 연체한 회원번호 와 책이름을 구하시오.
		단, 윤년은 무시한다. 
	[정답]
		연체한회원번호 :  1001  , 책제목 :  연필로쓰기
		연체한회원번호 :  1041  , 책제목 :  컴퓨터활용능력
'''

rentalList = [ 
	{"booknumber" : 20122, "bootsubject" : "연필로쓰기", "rentaldate" : "2020-11-25", "membernumber" : 1001},
	{"booknumber" : 40143, "bootsubject" : "외국어 공부의 감각", "rentaldate" : "2020-11-27", "membernumber" : 1003},
	{"booknumber" : 54321, "bootsubject" : "컴퓨터활용능력", "rentaldate" : "2020-11-27", "membernumber" : 1041},
	{"booknumber" : 26543, "bootsubject" : "아무튼,외국어", "rentaldate" : "2020-12-01", "membernumber" : 1034},
]

memberList = [ 
	{"membernumber" : 1001 , "booknumber" : 20122 , "rentalperiod" : 12},
	{"membernumber" : 1003 , "booknumber" : 40143 , "rentalperiod" : 8},
	{"membernumber" : 1041 , "booknumber" : 54321 , "rentalperiod" : 9},
	{"membernumber" : 1034 , "booknumber" : 26543 , "rentalperiod" : 2},
]

monList = [31,28,31,30,31,30,31,31,30,31,30,31]
today = [2020,12,4]
# today = [2021,1,4]


for i in range(len(rentalList)):
	for j in range(len(memberList)):
		if rentalList[i]['membernumber'] == memberList[j]['membernumber']:
			rentalList[i]['rentalperiod'] = memberList[j]['rentalperiod']

# for i in rentalList:
# 	print(i)

for i in range(len(rentalList)):
	rentDate = rentalList[i]['rentaldate'].split('-')
	tmp = []
	for j in rentDate:
		tmp.append(int(j))
	rentDate = tmp

# print(rentDate)
oneYear = 0
for i in monList:
	oneYear += i

# 오늘일자 총일수 구하기
todayTotal = 0
# 년
todayTotal += oneYear * (today[0] - 1)
# 월
for i in range(today[1] - 1):
	todayTotal += monList[i]
# 일
todayTotal += today[2]

# print(todayTotal)

# 빌린일수 구하기
for i in range(len(rentalList)):
	rentDayTotal = 0

	# 빌린날짜 배열로 변경
	rentalDate = rentalList[i]['rentaldate'].split('-')
	tmp = []
	for j in rentalDate:
		tmp.append(int(j))
	rentalDate = tmp

	# 빌린날짜기준 총일수
	rentDayTotal += oneYear * (rentalDate[0] - 1)
	for j in range(rentalDate[1] - 1):
		rentDayTotal += monList[j]
	rentDayTotal += rentalDate[2]
	
	# 빌린일수
	rentedTotal = todayTotal - rentDayTotal

	rentalList[i]['rentedTotal'] = rentedTotal
	
for i in rentalList:
	print(i)
print(today)

# 연체한 회원번호와 책이름
for i in range(len(rentalList)):
	if rentalList[i]['rentalperiod'] < rentalList[i]['rentedTotal']:
		print(rentalList[i]['membernumber'], rentalList[i]['bootsubject'])















# 정답
# for i in range(len(rentalList)):
# 	rental = rentalList[i]
# 	date = rental["rentaldate"]
# 	temp = date.split("-")
# 	year = int(temp[0])
# 	mon = int(temp[1])
# 	day = int(temp[2])
# 	rentaltotal = int(temp[0]) * 365;
# 	todaytotal = today[0] * 365;	
    
# 	for j in range(len(monList)):
# 		# print(mon , " " , j)
# 		if mon > j :
# 			rentaltotal += monList[j]
# 		if today[1] > j:
# 			todaytotal  += monList[j]
	
# 	rentaltotal += day
# 	todaytotal += today[2]
# 	for j in range(len(memberList)):
# 		member = memberList[j]
# 		if(member["booknumber"] == rental["booknumber"]):
# 			rentaltotal += member["rentalperiod"];
# 			break
# 	if rentaltotal > todaytotal:
# 		print("연체한회원번호 : " , member["membernumber"] , " , 책제목 : " , rental["bootsubject"])
     

