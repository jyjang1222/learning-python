import random
"""
	[1 to 50]
	   1. 구글에서 1 to 50 이라고 검색한다.
	   2. 1 to 50 순발력 게임을 선택해 게임을 실습해본다.
	   3. 최대한 비슷하게 만들기 
"""

# dict = {'front': 1, 'back': 25}
front = []
back = []

# for i in range(1, 26):
# 	front.append(i)
# for i in range(26, 51):
# 	back.append(i)

for i in range(1, 6):
	front.append(i)
for i in range(6, 11):
	back.append(i)

for i in range(1000):
	j = random.randint(0, len(front)-1)
	k = random.randint(0, len(front)-1)
	tmp1 = front[j]
	front[j] = front[k]
	front[k] = tmp1
	tmp2 = back[j]
	back[j] = back[k]
	back[k] = tmp2

# print(front)
# print(back)

field = []

for i in range(len(front)):
	dict = {}
	dict['front'] = front[i]
	dict['back'] = back[i]
	field.append(dict)


def printField(dictArr):
	for dict in dictArr:
		print(dict['front'], end=" ")

i = 1
while i <= 50:
	# 출력
	printField(field)
	inputNum = int(input('\n없앨 숫자를 입력하세요. \n'))

	for j in range(len(field)):
		if field[j]['front'] == inputNum and i == inputNum:
			if field[j]['front'] == field[j]['back']:
				field[j]['front'] = '0'
				del field[j]
				i += 1
				break

			field[j]['front'] = field[j]['back']
			i += 1

	if len(field) == 0:
		break
