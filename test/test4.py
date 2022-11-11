import random
# 1

r1 = random.randint(1, 6)
r2 = random.randint(1, 6)

r3 = random.randint(1, 6)
r4 = random.randint(1, 6)


sum1 = r1 + r2
sum2 = r3 + r4

a = 0
b = 0

sel = random.randint(0, 1)
if sel == 0:
    a = sum1
elif sel == 1:
    a = sum2

sel = random.randint(0, 1)
if sel == 0:
    b = sum1
elif sel == 1:
    b = sum2


# 하나는 홀수 하나는 짝수
if (a % 2 == 1 and b % 2 == 0) or (a % 2 == 0 and b % 2 == 1):
    print(a, b, "비김")
# 둘다 짝수
if a % 2 == 0 and b % 2 == 0:
    if a > b:
        print(a, b, "a승리")
    elif a < b:
        print(a, b, "b승리")
    else:
        print(a, b, "비김")
# 둘다 홀수
if a % 2 == 1 and b % 2 == 1:
    if a > b:
        print(a, b, "b승리")
    elif a < b:
        print(a, b, "a승리")
    else:
        print(a, b, "비김")


# 하나는 홀수 하나는 짝수
# if r1 % 2 == 1 and r2 % 2 == 0 or r1 % 2 == 0 and r2 % 2 == 1:
#     print(r1, r2, "비김")
# 둘다 짝수
# if r1 % 2 == 0 and r2 % 2 == 0:
#     if r1 > r2:
#         print(r1, r2, "r1승리")
#     elif r1 < r2:
#         print(r1, r2, "r2승리")
#     else:
#         print(r1, r2, "비김")
# 둘다 홀수
# if r1 % 2 == 1 and r2 % 2 == 1:
#     if r1 > r2:
#         print(r1, r2, "r2승리")
#     elif r1 < r2:
#         print(r1, r2, "r1승리")
#     else:
#         print(r1, r2, "비김")

# 2
count4 = 0
count8 = 0

for i in range(1, 100):
    if i <= 10:
        if i % 10 == 4:
            count4 += 1
            print(i, end = " ")
        if i % 10 == 8:
            count8 += 1
            print(i, end = " ")
    if i >= 10:
        if i // 10 == 4:
            count4 += 1
            print(i, end = " ")
            if i % 10 == 8:
                count8 += 1
            if i % 10 == 4:
                count4 += 1
                print(i, end = " ")
        if i // 10 == 8:
            count8 += 1
            print(i, end = " ")
            if i % 10 == 8:
                count8 += 1
                print(i, end = " ")
            if i % 10 == 4:
                count4 += 1

print()
print(count4, count8)
