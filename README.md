# python 문제풀이 모음

## 중요 문제

### 나머지 응용<br>(특정자리 구하기)

```python
# 가운데숫자 구하기

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
```

### 나머지 응용<br>(특정 범위에서 계속 루프하는 수 구하기)

```python
# 루프하는 수
while True:
    n = 0

    # 01 루프
    loop1 = n % 2

    # 012 루프
    loop2 = n % 3

    n += 1
```

### 배열 예외처리하는 방법

<b>배열에서 반복문으로 값의 체크가 필요한데 배열의 범위를<br>벗어나는 반복문일때 벗어나는 부분만 예외처리 하는 법</b>

```python
import random
'''
	[문제]
		세로 가로 인덱스 두 개를 랜덤으로 저장한다.
		그 인덱스를 기점으로 대각선 방향으로 전부
        1로 채운 후 출력하시오.

		[예]
			y = 2
			x = 1

			[0,0,0,1,0]
			[1,0,1,0,0]
			[0,1,0,0,0]
			[1,0,1,0,0]
			[0,0,0,1,0]
'''
list = [
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0]
]

y = random.randint(0, 4)
x = random.randint(0, 4)
print("y:",y,"x:",x)
list[y][x] = 1


# 1시방향
for k in range(len(list)):
	if y-k < 0 or x+k >= len(list):
		continue
	list[y-k][x+k] = 1
# 5시방향
for k in range(len(list)):
	if y+k >= len(list) or x+k >= len(list):
		continue
	list[y+k][x+k] = 1
# 7시방향
for k in range(len(list)):
	if y+k >= len(list) or x-k < 0:
		continue
	list[y+k][x-k] = 1
# 11시방향
for k in range(len(list)):
	if y-k < 0 or x-k < 0:
		continue
	list[y-k][x-k] = 1

for i in range(len(list)):
	print(list[i])
```

1. continue를 활용하면 손쉽게 예외처리가 가능하다

예외처리 할것이 많을때의 문제 예시

1. 이차배열5*문제09*구의개수\_문제
2. 이차배열5*문제11*체스비숍\_문제

### 날짜계산

```python

# 빌린일수 구하기
monList = [31,28,31,30,31,30,31,31,30,31,30,31]
today = [2020,12,12]
rentDate = [2020,11,30]

todayTotal = 0

oneYear = 0
for i in monList:
	oneYear += i

# 년
todayTotal += oneYear * (today[0] - 1)
# 월
for i in range(today[1] - 1):
	todayTotal += monList[i]
# 일
todayTotal += today[2]


rentDayTotal = 0
# 년
rentDayTotal += oneYear * (rentDate[0] - 1)
# 월
for i in range(rentDate[1] - 1):
	rentDayTotal += monList[i]
# 일
rentDayTotal += rentDate[2]

# 총일수 차이
rentedTotal = todayTotal - rentDayTotal
```

- 날짜의 총일수를 구하면 일수의 차이를 구할수 있다.
- 총일수의 날짜를 구할때는 몫과 나머지 계산을 활용한다.
