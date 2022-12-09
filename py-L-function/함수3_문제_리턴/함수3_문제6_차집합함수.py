"""
	[문제]
		a와  b를 매개변수로 받아서 
		서로 겹치지않는 값만 배열로 만들어서 반환해주는 함수를 만드시오.
		단, 한번저장된값은 중복하여저장되지않는다.
	[정답]
        [32, 65]
"""
a = [12, 32, 32, 43, 65, 43]
b = [21, 12, 43, 2, 4, 5]

def getListNotDuplicatedValue(arr1, arr2):
	tmp = []
	for i in arr1:
		# 겹치는지체크
		chk = True
		for j in arr2:
			if i == j:
				chk = False
		if chk:
			# 저장할값 중복체크
			chk2 = True
			for k in tmp:
				if i == k:
					chk2 = False
			if chk2:
				tmp.append(i)
	return tmp

res = getListNotDuplicatedValue(a, b)
print(res)