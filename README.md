# 파이썬 이차반복문
## 기억해둘 개념문제
1. 이차반복1_개념04_출력세로  
>	[문제]  
>		랜덤(3~6)숫자 하나를 저장하고 그 숫자만큼 아래와 같은 규칙 출력하시오.  
>		단, 일차 반복문과 이차 반복문으로 출력하시오.  
> 	[예시1]  
>		r = 6  
>	[출력1]  
>		1 7 13  
>		2 8 14  
>		3 9 15  
>		4 10 16  
>		5 11 17  
>		6 12 18  
> 	[예시2]  
>		r = 3  
>	[출력2]  
>		1 4 7  
>		2 5 8  
>		3 6 9  


<pre><code>cnt = 0

i = 1
while True:
	if i == r + 1:
		break
	if cnt == 0:
		j = i
	print(j, end = " ")
	cnt += 1
	if cnt == 3:
		print()
		cnt = 0
		i += 1
	j += 6
</code></pre>

일차반복문만 쓴 풀이를 잘 기억해두자  

<pre><code>for i in range(1, r + 1):
	for j in range(i, i + 12 + 1, 6):
		print(j, end = " ")
	print()
</code></pre>
  
위의 코드는 i + 12 + 1 같이 for in의 반복 범위를  
생각해내기가 까다롭다

<pre><code>cnt = 0

for i in range(1, r + 1):
	j = i
	while True:
		print(j, end = " ")
		cnt += 1
		if cnt == 3:
			cnt = 0
			break
		j += 6
	print()
</code></pre>
  
그러므로 세로길이가 확실한 첫반복문만 for in 을 사용하고  
반복범위를 생각하기 어려운부분은 while문을 사용하자  

## 다시 풀어볼 문제
1. 이차반복2_개념02_자기비교
2. 이차반복4_문제02_단일출력_문제