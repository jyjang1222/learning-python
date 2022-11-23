'''
    [문제]
        a리스트의 값들을 두 개씩 더해서 하나로 합친다.
        각 가로를 기준으로 보았을 때,  
        0번과 1번을 합친고,
        2번과 3번을 합친고,
        4번과 5번을 합친다.
        
        위와 같은 방법으로 남은 두 줄도 반복하면 된다.
    [예시]
        [ 3, 1, 2, 5, 6, 1] : [4,7,7]
        [ 2, 5, 1, 3, 5, 4] : [7,4,9]
        [ 1, 2, 1, 3, 9, 5] : [3,4,14]
    [정답] 
        [4, 7, 7]
        [7, 4, 9] 
        [3, 4, 14]
'''
a = [
    [ 3, 1, 2, 5, 6 ,1],
    [ 2, 5, 1, 3, 5 ,4], 
    [ 1, 2, 1, 3, 9 ,5] 
]

b = []

for i in range(len(a)):
    sum = 0
    cnt = 0
    tmp = []
    for j in range(len(a[i])):
        sum += a[i][j]
        cnt += 1
        if cnt >= 2:
            tmp.append(sum)
            cnt = 0
            sum = 0
    b.append(tmp)

print(b)

b = []

for i in range(len(a)):
    sum = 0
    tmp = []
    for j in range(len(a[i])):
        if j % 2 == 0:
            sum = a[i][j] + a[i][j + 1]
            tmp.append(sum)
    b.append(tmp)

print(b)