'''
   [문제]
      a 리스트에 있는 값들을 b에 저장하려고 한다. 
      a 리스트의 값을 뒤에서부터 두 개씩 저장하시오.
   [정답]
      b = [7,7,3,3,1,1]
'''

a = [1 ,3, 7]
b = [0, 0, 0, 0, 0, 0]

idxEnd = len(a) - 1
j = 0
k = 0

for i in range(len(b)):
   if i % 2 == 0 and i > 0:
      k += 1
   b[i] = a[idxEnd - k]
   
# b[0] = a[idxEnd]
# b[1] = a[idxEnd]
# b[2] = a[idxEnd - 1]
# b[3] = a[idxEnd - 1]
# b[4] = a[idxEnd - 2]
# b[5] = a[idxEnd - 2]

print(b)
