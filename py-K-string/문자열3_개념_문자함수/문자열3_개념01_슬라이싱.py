'''
    [문자열 슬라이싱]
        문자열을 자를 때 사용한다.
        여러 개를 한 번에 자를 수 있다.
        마지막 숫자는 세지 않는다.
        
    [1] 문자열[시작:마지막-1] : 마지막은 세지 않기 때문에 -1을 해야한다.
    
    [2] 문자열[:마지막-1] : 시작부터 마지막 -1까지 자른다.
    
    [3] 문자열[시작:] : 시작부터 마지막까지 자른다.
'''
#       0123456789
text = "java python javascript"

a = text[0:4]
print(a)   

b = text[:4]
print(b)

c = text[7:14]
print(c)

d =  text[7:]
print(d)

e = text[5:11]
print(e)

f = text[12:22]
print(f)
