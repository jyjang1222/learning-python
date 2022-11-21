'''
	[문제]	
		철수와 영희는 3월 3일에 만났다. 		
		철수는 영희와 100일 기념일에 축하 파티를 하려 한다.
		만난 지 100일 뒤는 몇 월 며칠인지 구하시오.
		단, 윤년은 계산하지 않으며,
		시작일은 포함시키지 않는다.
	[정답]
		6월 11일
'''

monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = 3
day = 3
meet = 0

# 달은 1부터시작이라서 1을 빼준다
for i in range(month - 1):
	meet += monthList[i]

meet += day
party = meet + 100


month = 1
day = 0
for i in range(len(monthList)):
	party -= monthList[i]
	month += 1
	if party - monthList[i] < 0:
		day = party
		break

print(month, day)

# month = 3
# day = 3

# total = 0
# for i in range(month - 1):
# 	total += monthList[i]
# total += day
# print("total =", total)

# total += 100
# print("total =", total)

# i = 0
# while True:
# 	temp = total
# 	total -= monthList[i]
# 	if total < 0 :
# 		print((i+1), temp)
# 		break
# 	i += 1
	



