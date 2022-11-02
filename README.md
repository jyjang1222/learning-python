# 파이썬 일차반복문
파이썬 일차반복문 문법과 문제풀이

## 배운사항
1. 파이썬에는 ++ -- 증감연산자가 없다.  
* 복합대입연산자를 활용해야한다
2. 아래와 같이 표현하면 줄 바꿈이 삭제되어 옆으로 출력된다.  
> print(변수)  ==> print(변수, end=" ")
3. print()에 아무것도 적지 않으면 그냥 줄 바꿈이 된다. 

## 궁금사항
Q. 복합대입연산을 c += (a + b) 이런식으로 써도 무난한지 ?  
A. 위의 식은 복잡해보이니 아래의 식이 직관적이다.  
> d = a + b  
> c += d

## 기억사항
1. 
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
2. 최대공약수  
공통으로 나누어떨어지는 수  
예) 16, 20의 최대공약수 4
3. 최소공배수  
공통으로 약수를 가지는 수  
예) 2, 3의 최소공배수 6  
(2, 3은 반드시 6의 약수가 된다)
4. 소수  
소수란, 1과 자기 자신으로만 나눠지는 수
예) 2, 3, 5, 7, 11, 13, ..
5. 반복문8_문제02_반복규칙찾기3_문제
증가량이 등차수열이면 변수를 활용
## 다시 풀어볼 문제
1. 반복문4_개념06_약수_직전직후
2. 반복문7_개념01_369게임
3. 반복문7_문제02_건물주
4. 반복문7_문제03_건물청소_문제
5. 반복문8_문제06_반복규칙찾기7_문제