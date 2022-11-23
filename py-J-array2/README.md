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


## 다시풀어볼문제
1. 이차배열2_개념03_정렬
2. 이차배열2_문제03_관리비_문제4  
--> 순위 구하기 풀이방식 학습필요  
3. 이차배열5_문제03_우회전_문제  
--> 회전 규칙 다시 생각