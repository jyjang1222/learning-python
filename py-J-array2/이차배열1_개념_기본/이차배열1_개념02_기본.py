'''
    [문제]
        b리스트에 1~9를 순차적으로 저장하고 출력하시오.
    [정답]
        b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
'''
b = [[0,0,0],[0,0,0],[0,0,0]]


k = 1
for i in range(len(b)):
    for j in range(3):
        b[i][j] = k
        k += 1

print(b)

for i in range(len(b)):
    print(len(b[i]))
    

# num = 1
# for i in range(len(b)):
#     for j in range(len(b[i])):
#         b[i][j] = num
#         num += 1

# print("b =", b)

