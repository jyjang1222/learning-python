# 파이썬 문자열 문제풀이

## 문자열 메서드 모음

- 메서드를 사용하고 변수에 넣어야 적용되는 것에 유의한다.

### replace() 메서드

```python
str = 'hello world'
str = str.replace('o', '', 1)
print(str) # hell world
```

- 값이 문자열일때 쓸수있는 메서드이다.
- 변경할 문자를 지정하고 다른 문자로 치환할수있다.
- replace(str, str, cnt)
- 인자는 차례로 변경될 문자, 치환할 문자, 수행횟수

### split() 메서드

- 문자열로 데이터를 저장할 때는 보통 구분자를 사용한다.
- 이런 문자열을 쉽게 리스트로 변환해주는 split() 함수가 있다.

```python
# [일차원 구분자]
text = "80,3,23"
a = text.split(",")
print(a) # ['80', '3', '23']

# [이차원 구분자]
text = "1001,김철수/1002,이민수/1003,신영희"
# 먼저 / 로 잘라낸다.
temp = text.split("/")
print(temp) # ['1001,김철수', '1002,이민수', '1003,신영희']
a = []
for i in range(len(temp)):
    # 각 데이터를 다시 ,를 기준으로 잘라낸다.
    temp2 = temp[i].split(",")
    a.append(temp2)

print(a) # [['1001', '김철수'], ['1002', '이민수'], ['1003', '신영희']]
```

## 문자열 문제 문법

### in, not in 키워드

```python
str = 'hello world'
bool = False
if 'hell' in str:
    bool = True
print(bool) # True
```

- 데이터 안에 값이 있는지없는지 반환하는 키워드이다.
- in 키워드는 안에 있으면 true반환 없으면 false반환 이고 not in은 그 반대이다.

### 문자열 슬라이싱

- 문자열을 자를 때 사용한다.
- 여러 개를 한 번에 자를 수 있다.
- 마지막 숫자는 세지 않는다.

1. 문자열[시작:마지막-1] : 마지막은 세지 않기 때문에 -1을 해야한다.
2. 문자열[:마지막-1] : 시작부터 마지막 -1까지 자른다.
3. 문자열[시작:] : 시작부터 마지막까지 자른다.

```python
text = "java python javascript"

a = text[0:4] # java

b = text[:4] # java

c = text[7:14] # thon ja

d =  text[7:] # thon javascript

e = text[5:11] # python

f = text[12:22] # javascript
```

### 문자열 비교

- 문자도 숫자와 같이 내부적으로 각각의 문자에 해당하는 숫자로 되어있다.
- 예를 들어 a가 1이면 b는 2이다.
- 그렇기떄문에 문자도 크다 작다로 비교할 수 있다.

```python
a = ["aa", "ee", "cc", "dd", "bb"]

if a[0] < a[4]:
    print(True)
```

### 문자열 구분자

## 다시 풀어볼 문제
