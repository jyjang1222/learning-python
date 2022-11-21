'''
    [문제]
        문자열 hello를 거꾸로 olleh로 출력하시오.
'''
text = "hello"

# 1
text = "olleh"

print(text)

# 2
text = "hello"
tmp = ""

for i in range(len(text)):
    tmp += text[len(text) - 1 - i]

print(tmp)
