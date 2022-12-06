'''
    [문제]
        a리스트는 단어들이 모여있는 리스트이다.
        search는 검색하고 싶은 단어이다.
        a리스트에서 해당 단어를 검색해서 출력하시오.
        단, 부분 검색도 되어야한다.
        
    [예시] 
        school, teacher, child
'''


a = ["school", "teacher", "child", "father", "love"]

search = "ch"

for i in range(len(a)):
    # for j in range(len(a[i])):
    for j in range(len(a[i]) - len(search)):
        cnt = 0
        # 검색
        for k in range(len(search)):
            # 검색범위 벗어나면 예외처리
            # if j + k > len(a[i]) - 1:
            #     continue
            if a[i][j+k] == search[k]:
                cnt += 1
        if cnt == len(search):
            print(a[i])