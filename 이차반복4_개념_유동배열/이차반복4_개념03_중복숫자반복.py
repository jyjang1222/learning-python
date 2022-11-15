import random
'''
	[문제]
		a리스트에 랜덤(1~4) 숫자 4개를 저장한다. 
		단, 중복없는 숫자로 저장한다.
	
	[예시]
		[1,4,2,3]
'''

a = []
# r = random.randint(1, 4)
# a.append(r)
cnt = 0

while cnt < 4:
	r = random.randint(1, 4)
	chk = True
	for j in range(len(a)):
		if a[j] == r:
			chk = False
			break
	if chk == True:
		a.append(r)
		cnt +=1

print(a)


















# 정답
# count = 0
# while True:
# 	r = random.randint(1,4)
# 	check = False
# 	for i in range(len(a)):
# 		if a[i] == r:
# 			check = True
# 			break
# 	if check == False:
# 		a.append(r)
# print(a)

