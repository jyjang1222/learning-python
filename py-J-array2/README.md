# 파이썬 이차배열 문제풀이
## 기억사항
<pre><code>b = [[0,0,0],[0,0,0],[0,0,0]]

num = 1
for i in range(len(b)):
    for j in range(len(b[i])):
        b[i][j] = num
        num += 1
</code></pre>
  
중첩된 배열의 길이 표현 : len(b[index])

## 다시풀어볼문제