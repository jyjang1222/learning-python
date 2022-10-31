# 파이썬 일차반복문
파이썬 일차반복문 문법과 문제풀이

## 배운사항
1. 파이썬에는 ++ -- 증감연산자가 없다.

## 궁금사항
Q. 복합대입연산을 c += (a + b) 이런식으로 써도 무난한지 ?  
A. 위의 식은 복잡해보이니 아래의 식이 직관적이다.  
> d = a + b  
> c += d

## 다시 풀어볼 문제

## 기억해둘 사항
[문제] 4~1 까지 거꾸로 출력하시오.  
[정답] 4 3 2 1

<pre><code> i = 4
while i >= 1:
    print(i)
    i -= 1
</code></pre>

위 방법보다는 아래 방법을 권장한다.  
반복 횟수를 파악하는데 아래 방법이 더 직관적이다.  
추가로 변수를 선언해서 원하는 값을 얻으면 된다.

<pre><code> i = 1
num = 4
while i <= 4:
    print(num)
    num -= 1
    i += 1
</code></pre>