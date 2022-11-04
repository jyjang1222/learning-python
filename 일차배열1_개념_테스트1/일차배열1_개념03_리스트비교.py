import random
'''
    [문제]
        a 와 b 를 각각 비교해서 더 큰 값을 출력한다. 
        서로 같으면 둘 다 출력한다.
    [정답]
        b :  54
        a :  43
        a :  23
        a :  12 , b :  12
        a :  53
'''
a = []
b = []

# a[0] = 2
# a[1] = 3

# a.append(2)
# a.append(3)

for i in range(5):
    num = random.randint(1, 99)
    a.append(num)
    num = random.randint(1, 99)
    b.append(num)
    if a[i] > b[i]:
        print(a[i], b[i], "큰 수", a[i])
    elif a[i] < b[i]:
        print(a[i], b[i], "큰 수", b[i])
    else:
        print(a[i], b[i], "수 같음")

# print(a)
# print(b)


# a = [10,43,23,12,53]
# b = [54,6,4,12,50]

# print("a : " , a)
# print("b : " , b)

# for i in range(len(a)):
#     if a[i] > b[i]:
#         print("a : " , a[i])
#     elif a[i] < b[i] : 
#         print("b : " , b[i])
#     else:
#         print("a : " , a[i] , ", b : " , b[i])


