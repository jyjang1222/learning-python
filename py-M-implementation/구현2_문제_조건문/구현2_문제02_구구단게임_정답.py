"""
    [문제]
        구구단 게임
        1. 구구단 문제를 출제하기 위해, 숫자 2개를 입력받는다.
        2. 입력받은 숫자를 토대로 구구단 문제를 출력한다.
        예)	3 x 7 = ?
        3. 문제에 해당하는 정답을 입력받는다.
        4. 정답을 비교 "정답" 또는 "땡"을 출력한다.
"""
a = input("구구단 숫자1을 입력 : ")
b = input("구구단 숫자2를 입력 : ")
message = a + " * " + b + " = "
print(message , end="")
c = input()
if int(a) * int(b) == int(c):
    print("정답")
else:
    print("오답")