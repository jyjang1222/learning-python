'''
	[문제1]
		a = [0,10,20,30,40,50]
		a리스트의 값들을 한칸씩 앞으로 당긴다.
	[예시]
		a = [10,20,30,40,50,0]
  
	[문제2]
		b =  [10,20,30,40,50,0]
		b리스트의 값들을 한칸씩 뒤로 민다.
  		b =  [0,10,20,30,40,50]
'''
a = [0,10,20,30,40,50]
i = 0
while i < len(a) - 1:
    a[i] = a[i + 1]
    i += 1
print(a)
a[len(a) - 1] = 0
print(a)

b =  [10,20,30,40,50,0]
i = len(b) - 1
while i >= 0:
    b[i] = b[i - 1]
    i -= 1
print(b)
b[0] = 0
print(b)
    




