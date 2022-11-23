'''
    [문제]
        a리스트는 압축하기 전 데이터이다.
        다음데이터를 압축 하시오.
        
        압축 기준은 데이터와 개수로 저장한다.
        예를 들어 3이 연속으로 5개이므로
        b = [[3,5]]
        다시 5가 6개이므로
        b = [[3,5],[5,6]]
        위와 같이 마지막까지 반복하시오.  
    [정답]     
        [3, 5]
        [5, 6]
        [2, 1]
        [4, 1]
        [2, 2]
'''
a = [3,3,3,3,3,5,5,5,5,5,5,2,4,2,2]
b = []

tmp = []
prev = a[0]
cnt = 1

for i in range(1, len(a)):
    if prev == a[i]:
        cnt += 1
    if prev != a[i] or i == len(a) - 1:
        tmp.append(prev)
        tmp.append(cnt)
        cnt = 1
    prev = a[i]

print(tmp)

tmp2 = []
cnt = 0
for i in range(len(tmp)):
    tmp2.append(tmp[i])
    cnt += 1
    if cnt == 2:
        b.append(tmp2)
        tmp2 = []
        cnt = 0
print(b)