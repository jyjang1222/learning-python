# python 문제풀이 모음
## 중요한 기억사항
### 나머지 구하기 응용 (특정자리 구하기)
<pre><code># 가운데숫자 구하기

n = 12345
center = n // 2 + 1
for i in range(center):
    n %= 10
    res = n
    n //= 10

print(res)
</code></pre>

### 나머지 구하기 응용 (특정 범위에서 계속 루프하는 수 구하기)
<pre><code># 루프하는 수 
while True:
    n = 0

    # 01 루프
    loop1 = n % 2

    # 012 루프
    loop2 = n % 3

    n += 1

</code></pre>