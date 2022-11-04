import random
'''
	[문제]
		랜덤으로 리스트의 값을 교환하고, 출력하시오.  
		[예]
			교환 전  [10,20,30,40,50,60,70,80] : 30과 40을 교환
			교환 후  [10,20,40,30,50,60,70,80]
'''

a = [10, 20, 30, 40, 50, 60, 70, 80]
print("교환 전 =", a)

idx1 = random.randint(1, len(a))
idx2 = random.randint(1, len(a))
tmp = 0

tmp = a[idx1]
a[idx1] = a[idx2]
a[idx2] = tmp

print("교환 숫자:", a[idx1], a[idx2])
print("교환 후 =", a)
