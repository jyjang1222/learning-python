import random

# 1
r = random.randint(3, 7)
print(r)

bool = True


for i in range(r):
    cnt = 0
    for j in range(5):
        n = 0
        # i가 홀수일때 j가 홀수이면 n = 1
        if i % 2 == 1:
            if j % 2 == 1:
                n = 1
            print(n, end = " ")
        # i가 짝수일때 j가 짝수이면 n = 1
        if i % 2 == 0:
            if j % 2 == 0:
                n = 1
            print(n, end = " ")
        cnt += 1
        if cnt == 5:
            print()
