'''
	[문제] 	
		현재 택시는 5, 5 위치에 있다.
		배열의 왼쪽 세로줄은 속도를 뜻한다.
		배열의 오른쪽 세로줄은 방향을 뜻하고 (북, 동, 남, 서)를 뜻한다. 
		
		속도와 방향은 택시가 매번 이동한 내용을 기록한 것이다. 
		
		예) 속도는 4이고 방향은 북쪽을 뜻한다. 
			y가 4증가해  x : 5 , y : 9 가 된다.  
			
		6번 모두 이동한 후 택시의 위치를 출력하시오. 
	[정답]
		x : -1 y : 8
'''
arr = [
		[4, "북"],
		[2, "동"],
		[1, "남"],
		[5, "서"],
		[4, "서"],
		[1, "동"]
	]
x = 5
y = 5

NORTH = '북'
EAST = '동'
SOUTH = '남'
WEST = '서'

for i in range(len(arr)):
	if arr[i][1] == NORTH:
		y += arr[i][0]
	elif arr[i][1] == EAST:
		x += arr[i][0]
	elif arr[i][1] == SOUTH:
		y -= arr[i][0]
	elif arr[i][1] == WEST:
		x -= arr[i][0]

print(x, y)