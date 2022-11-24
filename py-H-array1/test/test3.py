import random

a = [
    11,12,13,14,
    15,16,17,18,
    19,20,21,22]
# 0
# 4
# 8
r = random.randint(11, 22)
# r = 14
idx = 0

for i in range(len(a)):
    if a[i] == r:
        idx = i

# 행과 열은 1부터 시작이라 + 1
row = idx // 4 + 1
col = idx % 4 + 1

print(r, idx, row, col)
