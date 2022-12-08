'''
    [문제]
        arr리스트의 값을 체크하여
        짝수의 개수를 출력하는 함수를 만드시오.
    [정답]
        2
'''
arr = [2, 45, 1, 12]

def evenCount(arr):
    count = 0
    for i in arr:
        if i % 2 == 0 and i != 0:
            count += 1
    print(count)

evenCount(arr)