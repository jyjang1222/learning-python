import random

a = []
count = 0
check = True

while True:
    if check == True:
        r = random.randint(1, 30)
        if r % 2 != 0:
            a.append(r)
            count += 1
        check = False
  
    r = random.randint(1, 30)
    if r % 2 != 0:
        for i in range(len(a)):
            while a[i] == r:
                r = random.randint(1, 30)
                
        a.append(r)
        print(a, count)
        count += 1
    
    if count == 10:
        break

print(a)