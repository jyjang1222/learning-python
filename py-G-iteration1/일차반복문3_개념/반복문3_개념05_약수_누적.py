'''
[문제]
	18의 약수를 출력하고, 전체 합을 구하시오.
[정답]
	1 2 3 6 9 18 
	합 = 39
'''

# 풀이

num = 18
i = 1
sum = 0

while i <= 18:
	if num % i == 0:
		sum += i
	i += 1

print(sum)



# num = 18
# total = 0

# i = 1
# while i <= num:
# 	if num % i == 0:
# 		print(i, end=" ")
# 		total += i
# 	i += 1

# print()
# print("total =", total)