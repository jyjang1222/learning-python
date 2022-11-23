'''
    [문제]
        data의 각 숫자만큼 graph에 숫자1을
        세로로 아래에서 위로 채우시오.
    [정답]
        [0,0,0,0,1,0],
        [0,0,0,0,1,0],
        [0,0,0,0,1,0],
        [0,1,0,0,1,0],
        [0,1,0,0,1,0],
        [0,1,1,0,1,0],
        [0,1,1,0,1,1],
        [1,1,1,0,1,1],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1],
'''
data = [3,7,5,2,10,4]
graph = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
]

for i in range(len(graph[0])):
    for j in range(len(graph) - 1, (len(graph) - 1) - data[i], -1):
        graph[j][i] = 1
    # 정답
    # for j in range(data[i]):
    # graph[len(graph) - 1 - j][i] = 1

for i in range(len(graph)):
    print(graph[i])