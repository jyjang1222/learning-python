import random
'''
   [문제]
      a리스트에 랜덤(1~4) 숫자 4개를 저장한다. 
      단, 중복없는 숫자로 저장한다.
   
   [예시]
      [1,4,2,3]
'''

a = []

while True:
   if len(a) == 4:
      break

   r = random.randint(1, 4)
   chk = False

   for i in a:
      if i == r:
         chk = True
         break
         
   if chk == False:
      a.append(r)

print(a)















# a = [0, 0, 0, 0]
# check = [False, False, False, False]

# count = 0
# while True:
#    r = random.randint(0, 3)

#    if check[r] == False:
#       a[count] = r + 1
#       check[r] = True
#       count += 1

#    if count == 4:
#       break

# print(a)