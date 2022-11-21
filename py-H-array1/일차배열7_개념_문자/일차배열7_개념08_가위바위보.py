"""
    [문제]
        아래는 두학생의 가위바위보 데이터이다. 
        철수는 몇번 승리했는지 출력하시오.
"""
철수 = ["가위" , "바위" , "바위" , "보" , "가위"]
민수 = ["보" ,"가위" ,"바위" , "가위" , "보"]

count = 0

for i in range(len(철수)):
    # 비김
    if 철수[i] == 민수[i]:
        pass
    # 이김
    elif 철수[i] == "가위" and 민수[i] == "보":
        count += 1
    elif 철수[i] == "바위" and 민수[i] == "가위":
        count += 1
    elif 철수[i] == "보" and 민수[i] == "바위":
        count += 1
    # 졌을때
    else:
        pass

print(count)



# wincount = 0

# for i in range(len(철수)):
#     a = 철수[i]
#     b = 민수[i]

#     if a == b:
#         print("비김")
#     elif a == "가위" and b == "보":
#         print("이김")
#         wincount += 1
#     elif a == "바위" and b == "가위":
#         print("이김")
#         wincount += 1
#     elif a == "보" and b == "바위":
#         print("이김")
#         wincount += 1
#     else:
#         print("짐")

# print(wincount)
