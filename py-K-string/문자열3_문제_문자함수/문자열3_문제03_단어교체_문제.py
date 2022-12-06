'''     
    [문제]
        text변수의 내용을 변경하려 한다.
        change변수의 앞부분은 교체할 단어이고, 뒷부분은 삽입할 단어이다.
        text변수의 내용을 변경하시오.
    [정답]
        text = "Life is too short." (변경 전)          
        text = "Life is too long."  (변경 후)
'''


text = "Life is too short."
change = "short,long"


text2 = text[:-1] # . 제외
arr = text2.split(' ')
seed = change.split(',')
print(arr)

for i in range(len(arr)):
    if arr[i] == seed[0]:
        arr[i] = seed[1]

print(arr)

changedText = ''

for i in range(len(arr)):
    changedText += arr[i]
    if i != len(arr) - 1:
        changedText += ' '

changedText += '.'

print(changedText)

