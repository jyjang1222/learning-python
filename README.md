# python 문제풀이 모음
## 중요한 기억사항
### 나머지 응용<br>(특정자리 구하기)
<pre><code># 가운데숫자 구하기

n = 12345
tmp = n
cnt = 0
while True:
    if tmp == 0:
        break
    tmp //= 10
    cnt += 1

tmp = n
center = cnt // 2 + 1
for i in range(center):
    res = tmp % 10
    tmp //= 10

print(res)

</code></pre>

### 나머지 응용<br>(특정 범위에서 계속 루프하는 수 구하기)
<pre><code># 루프하는 수 
while True:
    n = 0

    # 01 루프
    loop1 = n % 2

    # 012 루프
    loop2 = n % 3

    n += 1

</code></pre>