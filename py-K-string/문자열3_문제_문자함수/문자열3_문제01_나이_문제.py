'''
    [문제]
        아래 주민번호를 가진 사람의 
        나이와 성별을 구하시오.
    [정답]
        35세
        남성
'''
jumin = "870612-1012940"

arr = jumin.split('-')

age = arr[0]
age = age[:2]
print(age)
MALE = 0
FEMALE = 1

gender = arr[1]
gender = int(gender[:1])

if gender == MALE:
    print("남성")
elif gender == FEMALE:
    print("여성")

