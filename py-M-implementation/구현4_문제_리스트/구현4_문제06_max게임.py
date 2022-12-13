"""
	[max게임]
	   
	    1. 가장 큰 값을 찾아 입력한다.
	    2. 정답이면 해당 값을 0으로 변경한다.
	    3. arr배열의 모든 값이 0으로 변경되면 프로그램은 종료된다.
	   	4. 가장큰값이 아닌 인덱스를 선택하면 아무일도 안생긴다.
"""


a = [10,54,345,656,87]

def chkZero(arr):
	chk = True
	for i in arr:
		if i != 0:
			chk = False
	return chk

def findMax(arr):
	max = 0
	for i in arr:
		if i > max:
			max = i
	return max

def findMaxIdx(arr, val):
	idx = 0
	for i in range(len(arr)):
		if arr[i] == val:
			idx = i
	return idx

while True:
	max = findMax(a)
	maxIdx = findMaxIdx(a, max)

	print(a)
	userInput = int(input('가장 큰 값을 입력하세요.\n'))
	if userInput == max:
		a[maxIdx] = 0
	chk = chkZero(a)
	if chk:
		print(a)
		break