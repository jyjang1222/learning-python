'''
	[문제]
		현재 택시는 5, 5 위치에 있다.
	 	dir 배열은 뱡향을 뜻하고 0, 1, 2,3은 북, 동, 남, 서를 뜻한다. 
	 	
	 	speed 배열은 속도를 뜻한다.
	 	
	 	dir과 speed 배열은 택시가 매번 이동한 내용을 기록한 것이다. 
	 	6번 모두 이동한 후 택시의 위치를 출력해주는 함수를 만드시오.

	 	예) 
			처음에 dir이 0이니 북쪽을 뜻한다. 
	 	   	speed는 4이므로, y가 4증가해  x : 5, y : 9 가 된다.  
	 	   
	 	   	두번째는 dir 이 2이니 남을 뜻하고, speed는 2이므로 
	 	   	y가 2감소해  x : 5, y : 7이 된다. 
'''

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def printTaxiPos(dirArr, speedArr, x, y):
	for i in range(len(dirArr)):
		if dirArr[i] == NORTH:
			y += speedArr[i]
		elif dirArr[i] == EAST:
			x += speedArr[i]
		elif dirArr[i] == SOUTH:
			y -= speedArr[i]
		elif dirArr[i] == WEST:
			x -= speedArr[i]
	print(x, y)

speed = [4, 2, 1, 5, 4, 2]
dir = [0, 1, 3, 2, 2, 1]

x = 5
y = 5

printTaxiPos(dir, speed, x , y)