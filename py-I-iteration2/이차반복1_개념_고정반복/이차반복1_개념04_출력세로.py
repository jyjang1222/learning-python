import random
'''
	[문제]
		랜덤(3~6)숫자 하나를 저장하고 그 숫자만큼 아래와 같은 규칙 출력하시오.
		단, 일차 반복문과 이차 반복문으로 출력하시오.
 	[예시1]
		r = 6
	[출력1]
		1 7 13
		2 8 14
		3 9 15
		4 10 16
		5 11 17
		6 12 18
 	[예시2]
		r = 3
	[출력2]
		1 4 7
		2 5 8
		3 6 9	
'''

r = random.randint(3, 6)
print("r:", r)

# 1
# 1.1
# cnt = 0
# for i in range(1, r + 1):
# 	cnt += 1
# 	print(i, end = " ")
# 	i += 6
# 	cnt += 1
# 	print(i, end = " ")
# 	i += 6
# 	print(i, end = " ")
# 	cnt += 1
# 	if cnt % 3 == 0:
# 		print()

# 1.2
cnt = 0

i = 1
while True:
	if i == r + 1:
		break
	if cnt == 0:
		j = i
	print(j, end = " ")
	cnt += 1
	if cnt == 3:
		print()
		cnt = 0
		i += 1
	j += 6
	

print()
# 2
# 2.1
# for i in range(1, r + 1):
# 	for j in range(i, i + 12 + 1, 6):
# 		print(j, end = " ")
# 	print()

# 2.2
# i = 1
# while i <= r:
# 	j = i
# 	while True:
# 		print(j, end = " ")
# 		cnt += 1
# 		if cnt == 3:
# 			cnt = 0
# 			break
# 		j += 6
# 	print()
# 	i += 1

# 2.3
for i in range(1, r + 1):
	j = i
	while True:
		print(j, end = " ")
		cnt += 1
		if cnt == 3:
			cnt = 0
			break
		j += 6
	print()







# 정답
# r = random.randint(3, 6)
# print(r)
# for i in range(r):
#     a = i + 1
#     print(a + r * 0, a + r * 1 , a + r * 2)

# print("----")
# for i in range(r):
#     a = i + 1
#     for j in range(3):
#         print(a +  j * r, end=" ")
#     print()



