# 파이썬 조건문
파이썬 조건문 문법과 문제풀이

## 배운사항
1. 파이썬은 0 < num < 10 같은 문법이 허용된다.  
*파이썬만 허용되기때문에 쓰지 않는것이 좋다.

## 궁금했던 사항
Q. 조건문에서 식이 길어질 경우 쓰는 방식
A.  
<pre><code>
if (cond1 == 'val1' and cond2 == 'val2' and 
       cond3 == 'val3' and cond4 == 'val4'):
    do_something
</code></pre>
<pre><code>
if (   
       cond1 == 'val1' and cond2 == 'val2' and 
       cond3 == 'val3' and cond4 == 'val4'
   ):
    do_something

if    (cond1 == 'val1' and cond2 == 'val2' and 
       cond3 == 'val3' and cond4 == 'val4'):
    do_something
</code></pre>
## 다시풀어볼 문제
1. 조건문3_문제_랜덤369