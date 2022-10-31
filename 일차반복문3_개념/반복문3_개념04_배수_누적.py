'''
[문제]
	40~100 사이에 5의 배수만 출력한다.
	반복문 종료 후 5의 배수의 전체 합을 출력한다.
[정답]
	40 45 50 55 60 65 70 75 80 85 90 95 100 
	합 = 910
'''

# 풀이

sum = 0
i = 40

while i <= 100:
	print(i, end = " ")
	sum += i
	i += 5

print("합 = ", sum)




# total = 0

# i = 40
# while i <= 100:
# 	if i % 5 == 0:
# 		print(i, end=" ")
# 		total += i
# 	i += 1
# print()
# print("total =", total)
