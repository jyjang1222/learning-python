"""
	[문제]
		a리스트는 철수와 민수의 가위바위보 데이터이다. 
		왼쪽이 철수의 데이터이고 오른쪽이 민수의 데이터이다

		철수와 민수는 계단 50번째 에서 게임을 시작했으며, 아래의 규칙을따른다.
		[규칙]
			이기면 계단 5증가
			비기면 계단 1증가
			지면 계단 3감소 
		
  		철수의 변화하는 위치를 전부 pos리스트에 저장하시오.
	[정답]
		[50, 55, 52, 49, 50, 51, 56]

"""

    
pos = [50]
a = [
	["바위" , "가위"],
	["바위","보"],
	["보","가위"],
	["가위","가위"],
	["바위","바위"],
	["보","바위"]
]

SCISSORS = '가위'
ROCK = '바위' 
PAPER = '보'

def chkPos(posArr ,battleLog):
	currentPos = pos[0]
	for i in range(len(battleLog)):
		chulsu = battleLog[i][0]
		minsu = battleLog[i][1]
		# 무승부
		if chulsu == minsu:
			currentPos += 1
		# 이길때
		elif chulsu == SCISSORS and minsu == PAPER:
			currentPos += 5
		elif chulsu == ROCK and minsu == SCISSORS:
			currentPos += 5
		elif chulsu == PAPER and minsu == ROCK:
			currentPos += 5
		else:
			currentPos -= 3
		posArr.append(currentPos)


chkPos(pos, a)
print(pos)













# def gameStart(a , pos):
#     lastpos = pos[0]
#     for i in range(len(a)):
#         b = a[i][0]
#         c = a[i][1]
#         if b == c:
#             lastpos += 1
#         elif b == "가위" and c == "보":
#             lastpos += 5
#         elif b == "바위" and c == "가위":
#             lastpos += 5
#         elif b == "보" and c == "바위":
#             lastpos += 5
#         else:
#             lastpos -= 3
#         pos.append(lastpos)
# gameStart(a, pos)
# print(pos)