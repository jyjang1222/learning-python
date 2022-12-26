"""
   [숫자이동]
       1. a를 사각형으로 출력한다.
	   2. 각숫자는 기능이 있다. 
	   	 [1] 숫자8는 플레이어이다. 
	     [2] 숫자0은 이동할수있는 길이다. 
	     [3] 숫자1은 이동불가능한 벽이다. 
	     [4] 숫자3은 골인지점이다.
      
	   3. "1.left  2.right 3.up 4.down"
	   	  	번호를 입력받고 각 방향으로 한칸씩 이동 가능 
	   
	   4. 예를들어 left를 선택하면 왼쪽으로 한칸이동한다. 
    
	  		{1,1,1,1,1,
			 1,0,0,0,1,
			 1,8,0,0,1,
		     1,0,0,0,3,
			 1,1,1,1,1};
	 	 
	   5. 계속 이동하다가 숫자 3에 도착하면 종료.

"""

a = [
    1,1,1,1,1,
	1,0,0,0,1,
	1,8,0,0,1,
	1,0,0,0,3,
	1,1,1,1,1
 ]

LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4
WALL = 1
GOAL = 3
PLAYER = 8

pos = 11

def printMap(arr):
	for i in range(len(arr)):
		print(arr[i], end=' ')
		if i % 5 == 4:
			print()

while True:
	printMap(a)

	userInput = int(input('1.left  2.right 3.up 4.down\n'))
	
	if userInput == LEFT:
		if a[pos - 1] == WALL:
			print('이동불가')
			continue
		a[pos] = 0
		pos -= 1
	elif userInput == RIGHT:
		if a[pos + 1] == WALL:
			print('이동불가')
			continue
		a[pos] = 0
		pos += 1
	elif userInput == UP:
		if a[pos - 5] == WALL:
			print('이동불가')
			continue
		a[pos] = 0
		pos -= 5
	elif userInput == DOWN:
		if a[pos + 5] == WALL:
			print('이동불가')
			continue
		a[pos] = 0
		pos += 5

	if a[pos] == GOAL:
		a[pos] = PLAYER
		printMap(a)
		break
	a[pos] = PLAYER
	

