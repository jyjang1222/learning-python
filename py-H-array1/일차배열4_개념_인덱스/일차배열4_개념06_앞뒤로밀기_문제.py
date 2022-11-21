'''
	[문제1]
		a리스트의 값들을 한 칸씩 앞으로 당기고 출력하시오.
	[정답1]
		a = [10,20,30,40,50,0]
  
	[문제2]
		b리스트의 값들을 한 칸씩 뒤로 밀고 출력하시오.
	[정답2]
		b =  [0,10,20,30,40,50]
'''

# [문제1]
a = [0, 10, 20, 30, 40, 50]
idx = len(a) - 1
tmp = a[0]

for i in range(idx):
	a[i] = a[i + 1]

a[idx] = tmp
print(a)


# [문제2]
b =  [10, 20, 30, 40, 50, 0]
idx = len(b) - 1
tmp = b[idx]

for i in range(idx):
	b[idx] = b[idx - 1]
	idx -= 1

b[0] = tmp
print(b)




