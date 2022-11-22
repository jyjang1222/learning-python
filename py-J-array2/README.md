# 파이썬 이차배열 문제풀이
## 기억사항
1. 2차배열 내부배열 길이설정 
<pre><code>b = [[0,0,0],[0,0,0],[0,0,0]]

num = 1
for i in range(len(b)):
    for j in range(len(b[i])):
        b[i][j] = num
        num += 1
</code></pre>
  
중첩된 배열의 길이 표현 : len(b[index])  

2. n차배열을 다룰때 접근방법  
-> n차배열을 1차배열로 변환후 접근하면 쉽다  
예) 2차배열을 오름차순, 내림차순 정렬한다면  
2 -> 1 -> 정렬 -> 2

3. 순위 구하는 방법  
순위 = 1 + 자기자신보다 큰수의 갯수  
<pre><code>arr = [1000, 2100, 1300, 4100, 1000, 1000, 3000, 1600, 800]  

rank = []
for i in range(len(arr)):
    count = 1
    for j in range(len(arr)):
        if arr[j]> arr[i]:
            count += 1
    rank.append(count)
print(rank)
</code></pre>

3. 나머지 구하기 응용 (특정자리 구하기)
<pre><code># 가운데숫자 구하기

n = 12345
center = n // 2 + 1
for i in range(center):
    n %= 10
    res = n
    n //= 10

print(res)
</code></pre>

4. 나머지 구하기 응용 (특정 범위에서 계속 루프하는 수 구하기)
<pre><code># 루프하는 수 
while True:
    n = 0

    # 01 루프
    loop1 = n % 2

    # 012 루프
    loop2 = n % 3

    n += 1

</code></pre>


## 다시풀어볼문제
1. 이차배열2_개념03_정렬
2. 이차배열2_문제03_관리비_문제4  
--> 순위 구하기 풀이방식 학습필요 