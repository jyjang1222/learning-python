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

item = {"name" : "새우깡" , "price" : 1000}

if "name" in item:
    print(item["name"])
else:
    print("찾는값이 없습니다1.")

if "count" in item:
    print(item["count"])
else:
    print("찾는값이 없습니다2.")
```

- 데이터 안에 값이 있는지없는지 반환하는 키워드이다.
- in 키워드는 안에 있으면 true반환 없으면 false반환 이고 not in은 그 반대이다.
- 딕셔너리를 대상으로 사용하면 해당 key값이 있는지 확인이 가능하다.

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

## 딕셔너리

- 리스트에서는 인덱스가 자동으로 0,1,2 이처럼 순서대로 설정이 되지만, 딕셔너리는 리스트의 인덱스에 해당하는 부분을 내가 직접 설정할 수 있다.
- 중괄호{}로 표현하며, 리스트와 딕셔너리를 구분하기위해 리스트의 인덱스를 딕셔너리는 키 라고 표현한다.
- 콜론(:)을 중심으로 {키1 : 값1 , 키2 : 값2 , 키3 : 값3 }

```python
# 리스트의 예
a = [10, 20, 30] # 자동으로 0 , 1, 2 가 생성된다.

# 딕셔너리의 예
b = {0 : 10, 1 : 20 , 2 : 30} # 직접 인덱스를 설정해야한다.

# 리스트 개별 출력
for i in range(len(a)):
    print(a[i] , end=" ")
print()
```

### 배열과 딕셔너리의 차이

```python
# 어떤 학생의 번호 , 이름 , 국어 ,수학 , 영어점수를 표현한다고 할때,

a = [1003 , "김철수" , 100, 10, 30]
#  예를들어 리스트는 국어 점수를 출력하고싶다면 ,
print("리스트의 국어 : " , a[2]) # 직관적이지 않다.

# 딕셔너리는 리스트의 인덱스에 해당하는 키를 직접 설정할수있다.
b = {"number" : 1003 , "name" : "김철수" , "국어" : 100 , "수학" : 10 , "영어"  : 30}
print("딕셔너리의 국어 : " , b["국어"]) # 직관적이다.
```

### 추가와 삭제

```python
# [추가] 위 b딕셔너리에 "총점" 키를 추가하시오.
b["총점"] = b["국어"] + b["수학"] + b["영어"]
for i in b.keys():
    print(i  , b[i] , end=" ")
# number 1003 name 김철수 국어 100 수학 10 영어 30 총
점 140

#[삭제] 위 b딕셔너리에 "총점" 키를 삭제하시오.
del(b["총점"])
for i in b.keys():
    print(i  , b[i] , end=" ")
# number 1003 name 김철수 국어 100 수학 10 영어 30
```

- 새로운 속성을 정하고 값을 넣으면 자동으로 늘어난다.
- 삭제는 del 키워드를 사용한다. del(dict[key])

### 딕셔너리 응용

```python
studentList = []
info = {"이름":"김철수", "수학":100, "국어":32}
studentList.append(info)

info = {"이름":"이만수", "수학":11, "국어":84}
studentList.append(info)

info = {"이름":"박영희", "수학":95, "국어":58}
studentList.append(info)

# studentList = [{'이름': '김철수', '수학': 100, '국어': 32}, {'이름': '이만수', '수학': 11, '국어': 84}, {'이름': '박영희', '수학': 95, '국어': 58}]
```

- 딕셔너리는 단독으로 사용하기보다는 리스트와 함께 2차원 모양으로 사용된다.

### 빈 딕셔너리 만들기

- 빈 딕셔너리 만들기
    1. a = dict()
    2. b = {}
- 빈 리스트 만들기
    1. a = list()
    2. b = []

```python
a = dict()

a["number"] = 10001
a["name"] = "김철수"

b = {}
b["number"] = 10002
b["name"] = "이영수"

c = list()
c.append(10001)
c.append("김철수")

d = []
d.append(10002)
d.append("이영수")
```

## 딕셔너리 메서드 모음

### keys() 메서드

```python
# 딕셔너리 출력
keyList = b.keys() # 키만 리스트로 반환
print(keyList) # dict_keys([0, 1, 2])

# 딕셔너리 개별출력
for i in b.keys():
    print(b[i] , end=" ")
print() # 10 20 30
```

### values() 메서드

```python
# 딕셔너리 출력
valueList = b.values() # 값만 리스트로 반환
print(valueList) # dict_values([10, 20, 30])
```
### get()
- dict.get(key, default = None)
- 첫번째 인자로 key를 넣어주면 해당 key의 값을 반환해준다.
- 두번째 인자는 해당 키가 없을때 반환할 디폴트값을 설정해줄수 있다.

## None 값

```python
item = {"name" : "새우깡" , "price" : 1000}

value = item.get("name")
print(value) # 새우깡

value = item.get("count")
print(value) # None
```

- 파이썬에서는 Undefined, Null 구분하지않고 None으로 통칭한다.

## 다시 풀어볼 문제

1. 문자열3\_문제06\_말하기수열\_문제
