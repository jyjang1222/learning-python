import random
# 1
# r = random.randint(1, 9)
arr = []

for i in range(6):
    r = random.randint(1, 9)
    arr.append(r)

# arr = [5, 7, 6, 2, 3, 1]
tmp = arr[0]

print(tmp, end = "")

for i in range(1, len(arr)):
    if i % 2 == 1:
        print(" +", arr[i], end = "")
        tmp += arr[i]
    if i % 2 == 0:
        print(" -", arr[i], end = "")
        tmp -= arr[i]
    if i == len(arr) - 1:
        print()

print(tmp)
