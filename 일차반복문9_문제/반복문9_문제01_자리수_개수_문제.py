import random

'''
[문제]
	10000~99999 사이의 랜덤숫자를 저장하고 
	자리별숫자가 5 이상인 개수를 출력하시오.
	
		예) 19200 ==> 9 하나만 5 이상 ==> 1
		예) 98436 ==> 9,8,6, 세 개가 5 이상 ==> 3
'''


# 1차풀이
num = random.randint(10000, 99999)
count = 0

# if num % 100000 // 10000 >= 5:
# 	count += 1
# if num % 10000 // 1000 >= 5:
# 	count += 1
# ...
# if num % 10 // 1 >= 5:
# 	count += 1

# j = 100000
# i = 1
# while i <= 5:
# 	if num % j // (j / 10) >= 5:
# 		count += 1
# 	j /= 10
# 	i += 1

# print(num, count)

# 2차풀이
print(num)
while num != 0:
	if num % 10 >= 5:
		count +=1
	num //= 10

print(count)