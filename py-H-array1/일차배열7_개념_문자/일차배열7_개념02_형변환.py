'''
    [문자열 형변환]
        문자열은 숫자가 아니기 때문에 산술연산을 사용할 수 없다.
        문자열을 산술하기 위해서는 문자를 숫자로 변환해야 한다. 

        [1] 문자를 정수로 형변환
            변수 = int(문자)
        [2] 숫자를 문자로 형변환
            변수 = str(숫자)
'''
a = "10"
# print(a + 10) # 에러가 발생한다. 문자열은 숫자와 더하기를 할 수 없다.
# a = int(a)
# print(a + 10)
print(int(a) + 10)


b = 10
b = str(b)
print(b + "10") # 문자열로 변환되었기 때문에 더하기를 사용할 수 있고, 1010이 출력된다. 