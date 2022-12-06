'''
    [문제]
    	다음은 읽고, 말하기 수열의 규칙이다.
  
  		1, 11, 12, 1121, 122111, 112213
  
	 	첫번째 수열 : 1
	 	두번째 수열 : 1이 1개 = 11
	 	세번째 수열 : 1이 2개 = 12
	 	네번째 수열 : 1이 1개, 2가 1개 = 1121
	 	다섯번째 수열 : 1이 2개, 2가 1개, 1이 1개 = 122111
	 	여섯번재 수열 : 1이 1개, 2가 2개, 1이 3개 = 112213
'''

a = "1"
print(a)

for i in range(6):
	tmp = ''
	i = 0
	while i < len(a):
		cnt = 0
		for j in range(i, len(a)):
			if a[i] == a[j]:
				cnt += 1
			else:
				break
		tmp += a[i]
		tmp += str(cnt)
		i += cnt # 같은숫자 갯수 만큼 건너뜀
	a = tmp

	print(a)
		
		
