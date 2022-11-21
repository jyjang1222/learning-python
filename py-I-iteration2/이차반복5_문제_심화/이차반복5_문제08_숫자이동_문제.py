'''
	[문제]
		철수는 게임을 개발하고 있다.
		game리스트를 아래와 같이 사각형으로 출력한다.

		숫자8 은 현재 플레이어가 있는 자리이다.
		숫자0 은 플레이어가 이동할 수 있는 자리이다.
		숫자1 은 플레이어가 이동할 수 없는 벽이다.

		order리스트는 플레이어를 움직이기 위한 명령어들이다.
		숫자 1~4로 표현하고 북(1)동(2)남(3)서(4)를 뜻한다.

		order의 내용대로 플레이어가 이동하는 경로를 전부 출력하시오.
		벽 때문에 이동할 수 없을 때는 "이동 불가"를 출력하시오.
'''

game = [1,1,1,1,1,
	    1,0,0,0,1,
	    1,0,8,0,1,
	    1,0,0,0,1,
	    1,1,1,1,1]

order = [1,2,3,3,3,1,4,1]

idx = 0


print(idx)
# 북쪽한칸이동 idx -= 5
# 동쪽한칸이동 idx += 1
# 남쪽한칸이동 idx += 5
# 서쪽한칸이동 idx -= 1
# 이동가능공간 idx 6 ~ 8, 11 ~ 13, 16 ~ 18

for i in order:
	chk = True

	for j in range(len(game)):
		if game[j] == 8:
			idx = j

	tmp = idx

	if i == 1:
		tmp -= 5
	elif i == 2:
		tmp += 1
	elif i == 3:
		tmp += 5
	elif i == 4:
		tmp -= 1

	# 이동가능공간이 아니면~
	if not(6 <= tmp and tmp <= 8 or 11 <= tmp and tmp <= 13 or 16 <= tmp and tmp <= 18):
		chk = False

	if chk:
		game[idx] = 0
		game[tmp] = 8
		print(game, tmp)
	else:
		print("이동불가", tmp)