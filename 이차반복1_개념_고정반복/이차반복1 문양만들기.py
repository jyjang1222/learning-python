# 1

'''
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
'''
'''
반복문을 사용하시오
'''

bool = True

for i in range(5):
    count = 0
    for j in range(5):
        n = 0
        if bool == False:
            if j % 2 == 1:
                n = 1
            print(n, end = " ")
        if bool == True:
            if j % 2 == 0:
                n = 1
            print(n, end = " ")
        count += 1
        if count == 5:
            print()
            if bool == True:
                bool = False
            elif bool == False:
                bool = True
