'''
	[문제]
		a리스트의 각 값이 나머지 값들과 비교해서 서로 같으면 
		둘 다 0으로 변경하시오.
		[1] 값 0은 비교에서 무시한다. 
		[2] 자기 자리는 비교에서 무시한다.
	[예시]
		10 : [0,30,40,0,20,30,50]
  		30 : [0,0,40,0,20,0,50]
		40 : 
		 0 : 
		20 : 
		 0 : 
		50 : 
	[정답]
		[0,0,40,0,20,0,50]
'''

a = [10,30,40,10,20,30,50]

# 
for i in range(len(a)):
	print(a[i], end = ":")
	for j in range(len(a)):
		if i != j:
			if a[i] != 0 or a[j] != 0:
				if a[i] == a[j]:
					a[i] = 0
					a[j] = 0
	print(a)








# for i in range(len(a)):
#     for j in range(len(a)):
#         if i != j and a[i] != 0 and a[i] == a[j] :
#             a[i] = 0
#             a[j] = 0
            
# print(a)