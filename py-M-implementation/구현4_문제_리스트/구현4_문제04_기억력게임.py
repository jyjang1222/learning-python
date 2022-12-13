import random
"""
	[기억력 게임]
		
		1. 같은 글자가 적혀있는 카드 2장씩 5세트가있다. (총10장)
		2. 먼저 card 를 셔플한다. 
		3. card 에 있는 카드 2개를 선택한다. (마우스가없으므로 인덱스로 선택)
		4. 선택한카드 2장의 내용이 같으면 정답이고, 총 다섯번 다맞추면 게임종료.
		[조건] 
  			[1] 같은 인덱스 선택할수없다. 
			[2] 이미 선택해서 맞춘카드는 다시 선택할수없다.
		
"""

# card = ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'e', 'e' ]
card = [
	{'front': '*', 'back': 'a'},
	{'front': '*', 'back': 'a'},
	{'front': '*', 'back': 'b'},
	{'front': '*', 'back': 'b'},
	{'front': '*', 'back': 'c'},
	{'front': '*', 'back': 'c'},
	{'front': '*', 'back': 'd'},
	{'front': '*', 'back': 'd'},
	{'front': '*', 'back': 'e'},
	{'front': '*', 'back': 'e'}]

def showCardList():
	for i in card:
		print(i['front'], end = ' ')
	print()

# 셔플
for i in range(100):
	r1 = random.randint(0, len(card)-1)
	r2 = random.randint(0, len(card)-1)

	tmp = card[r1]
	card[r1] = card[r2]
	card[r2] = tmp

# 카드뒤집고 보기
def turnAndShowCard(dataList, idx):
	dataList[idx]['front'] = dataList[idx]['back']
	showCardList()

while True:
	showCardList()

	# 카드 선택
	idx1 = int(input('카드인덱스를 입력해주세요.\n'))
	turnAndShowCard(card, idx1)
	while True:
		idx2 = int(input('카드인덱스를 입력해주세요.\n'))
		if idx1 != idx2:
			break
		else:
			print('이미 선택된 카드입니다.')
	turnAndShowCard(card, idx2)

	# 같은 카드인지 체크
	if card[idx1]['front'] == card[idx2]['front']:
		if idx1 > idx2:
			del card[idx1]
			del card[idx2]
		else:
			del card[idx2]
			del card[idx1]
	else:
		card[idx1]['front'] = '*'
		card[idx2]['front'] = '*'
	# 지우개
	for i in range(5):
		print()
	# 종료
	if len(card) == 0:
		break