import random
'''
    [문제]
        랜덤으로 dir 리스트의 값을 d에 저장한다. 
        랜덤으로 count 에 2~4를 저장한다.
        d값의 방향으로 a리스트의 모든값이 count 숫자만큼 이동한다. 
        밀린값은 반대편으로 저장된다.
        
    [예시1]
        d = "북" 
        count = 2
        
    [결과1]          
        [1008,1009,1010,1011],
        [1000,1001,1002,1003],
        [1004,1005,1006,1007],
        
    [예시2]
        d = "서"
        count = 3
    [결과2]
        [1003,1000,1001,1002],
        [1007,1004,1005,1006],
        [1011,1008,1009,1010],
    
'''
dir = ["북" , "동" , "남" , "서"]
d = ""
a = [
    [1000,1001,1002,1003],
    [1004,1005,1006,1007],
    [1008,1009,1010,1011],
]


r = random.randint(0, 3)
r = 3
count = random.randint(2, 4)
d = dir[r]


if d == "북":
    for k in range(count):
        tmp = a[0]
        for i in range(len(a) - 1):
            a[i] = a[i + 1]
        a[len(a) - 1] = tmp

if d == "동":
    for k in range(count):
        for i in range(len(a)):
            tmp = a[i][len(a[i]) - 1]
            for j in range(len(a[i]) - 1, 0, -1):
                a[i][j] = a[i][j - 1]
            a[i][0] = tmp

if d == "남":
    for k in range(count):
        tmp = a[len(a) - 1]
        for i in range(len(a) - 1, 0, -1):
            a[i] = a[i - 1]
        a[0] = tmp
    
if d == "서":
    for k in range(count):
        for i in range(len(a)):
            tmp = a[i][0]
            for j in range(len(a[i]) - 1):
                a[i][j] = a[i][j + 1]
            a[i][len(a[i]) - 1] = tmp

print(d, count)
for i in range(len(a)):
    print(a[i])