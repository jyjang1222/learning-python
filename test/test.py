import random
# 가위바위보 하나빼기 게임
'''
가위 = 0 바위 = 1 보 = 2
둘이서 가위바위보를 두개낸후
하나를 골라내서 승부를 가른다
'''

# 가위바위보 2개내기
철수왼 = random.randint(0, 2)
철수오 = random.randint(0, 2)
영희왼 = random.randint(0, 2)
영희오 = random.randint(0, 2)

person = ["철수", "영희"]
r = ["가위", "바위", "보"]
hand = ["왼손", "오른손"]

# 철수와 영희의 가위바위보 츨력
# for k in range(2):
#     for i in range(3):
#         for j in range(3):
#             if 철수왼 == i and 철수오 == j:
#                 print(person[k], "는", r[i],"와", r[j],"를 냈다")
#             elif 철수왼 == i and 철수오 == j:
#                 print(person[k], "는", r[i],"와", r[j],"를 냈다")
#             elif 철수왼 == i and 철수오 == j:
#                 print(person[k], "는", r[i],"와", r[j]," 냈다")

# 철수의 가위바위보 츨력
for i in range(3):
    for j in range(3):
        if 철수왼 == i and 철수오 == j:
            print("철수는", r[i],"와", r[j],"를 냈다")
        elif 철수왼 == i and 철수오 == j:
            print("철수는", r[i],"와", r[j],"를 냈다")
        elif 철수왼 == i and 철수오 == j:
            print("철수는", r[i],"와", r[j]," 냈다")

# 영희의 가위바위보 츨력
for i in range(3):
    for j in range(3):
        if 영희왼 == i and 영희오 == j:
            print("영희는", r[i],"와", r[j],"를 냈다")
        elif 영희왼 == i and 영희오 == j:
            print("영희는", r[i],"와", r[j],"를 냈다")
        elif 영희왼 == i and 영희오 == j:
            print("영희는", r[i],"와", r[j]," 냈다")        

# 둘중선택
철수선택 = random.randint(0, 1)
영희선택 = random.randint(0, 1)

# 둘중선택 출력
if 철수선택 == 0:
    print("철수는 왼손의", r[철수왼],"를 선택했다")
elif 철수선택 == 1:
    print("철수는 오른손의", r[철수오],"를 선택했다")

if 영희선택 == 0:
    print("영희는 왼손의", r[영희왼],"를 선택했다")
elif 영희선택 == 1:
    print("영희는 오른손의", r[영희오],"를 선택했다")


if 철수선택 == 0:
    철수선택 = 철수왼
elif 철수선택 == 1:
    철수선택 = 철수오

if 영희선택 == 0:
    영희선택 = 영희왼
elif 영희선택 == 1:
    영희선택 = 영희오

# 승부가르기
if 철수선택 != 영희선택:
    if 철수선택 == 0:
        if 영희선택 == 1:
            print("철수:", r[철수선택], "영희:", r[영희선택], "영희승")
        elif 영희선택 == 2:
            print("철수:", r[철수선택], "영희:", r[영희선택], "철수승")
    if 철수선택 == 1:
        if 영희선택 == 0:
            print("철수:", r[철수선택], "영희:", r[영희선택], "철수승")
        elif 영희선택 == 2:
            print("철수:", r[철수선택], "영희:", r[영희선택], "영희승")
elif 철수선택 == 영희선택:
    print("철수:", r[철수선택], "영희:", r[영희선택], "무승부")