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

### 배열 예외처리하는 방법
<b>배열에서 반복문으로 값의 체크가 필요한데 배열의 범위를<br>벗어나는 반복문일때 벗어나는 부분만 예외처리 하는 법</b>
<pre><code>arr = [1,1,7,1,7,7,7]

for i in range(len(arr) - 2):
    count = 0
    for j in range(3):
        if i+j >= len(arr):
            continue
        if arr[i+j] == 7:
            count += 1
    if count == 3:
        print("당첨")
</code></pre>
  
> len(arr) - 2
  
위의 코드에서는 예외처리를 위해 반복문의 범위를  
일일히 계산해줘야 한다
  
<pre><code>arr = [1,1,7,1,7,7,7]

for i in range(len(arr)):
    count = 0
    for j in range(3):
        if i+j >= len(arr):
            continue
        if arr[i+j] == 7:
            count += 1
    if count == 3:
        print("당첨")
</code></pre>
  
> if i+j >= len(arr):  
> <pre>    continue</pre>
  
continue를 활용하면 손쉽게 예외처리가 가능하다