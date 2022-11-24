arr = [1,1,7,1,7,7,7]

for i in range(len(arr) - 2):
    count = 0
    for j in range(3):
        if arr[i+j] == 7:
            count += 1
    if count == 3:
        print("당첨")


arr = [1,1,7,1,7,7,7]

for i in range(len(arr)):
    count = 0
    for j in range(3):
        if i+j >= len(arr):
            continue
        if arr[i+j] == 7:
            count += 1
    if count == 3:
        print("당첨")