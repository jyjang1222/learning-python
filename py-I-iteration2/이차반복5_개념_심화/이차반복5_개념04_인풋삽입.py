'''
	[문제]
		a리스트에 value값 3개를 추가하려고 한다.
		단, a리스트 마지막에 추가하는것이 아니고,
		index리스트의 위치에 추가하고, 위치 뒤의 모든 값은
		한칸씩 뒤로 이동한다. 
	[예시]
		index : 2 , value = 60 , a = [10,20,60,30,40,50]
		index : 1 , value = 70 , a = [10,70,20,60,30,40,50]
		index : 0 , value = 80 , a = [80,10,70,20,60,30,40,50]
	[정답]
		a = [80, 10, 70, 20, 60, 30, 40, 50]
'''
a = [10,20,30,40,50]
idx = [2,1,0]
val = [60,70,80]
tmp = 0
# [10,20,30,40,50,60]
# [10,20,60,30,40,50]

for i in range(len(idx)):
	# val값 a마지막에넣음
	a.append(val[i])
	j = len(a) - 1
	# 인덱스 값 까지 끝에 넣은 val값 옮기기
	while j > idx[i]:
		tmp = a[j - 1]
		a[j - 1] = a[j]
		a[j] = tmp
		j -= 1
	print(a)

# print(a)












# 정답
# a = [10,20,30,40,50]

# for i in range(3):
# 	a.append(val)

# 	j = len(a) - 1
# 	while j > idx[i]:
# 		a[j] = a[j - 1]
# 		j -= 1
	
# 	a[idx[i]] = val[i]

# print(a)
