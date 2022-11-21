import random
'''
	[문제]
		랜덤(3~6)숫자 하나를 저장하고 그 숫자만큼 아래와 같이 출력하시오.
		단, 아래 일차 반복문과 이차 반복문으로 출력하시오.
 	[예시1]
		r = 6
	[출력1]
		1 2 3
		2 3 4
		3 4 5
		4 5 6
 	[예시2]
		r = 4
	[출력2]
		1 2 3
		2 3 4		
'''

r = random.randint(3, 6)
print(r)

cnt = 0

i = 1
while True:
	print(i, end =" ")
	cnt += 1
	if i == r:
		break
	if cnt == 3:
		print()
		cnt = 0
		i -= 2
	i += 1

print()


i = 1
# i <= r - 2
while i <= r - 2:
	cnt = 0
	j = i
	while cnt < 3:
		print(j, end = " ")
		cnt += 1
		if cnt == 3:
			print()
		j += 1
	i += 1





# r = random.randint(3, 6)
# print("r : " , r)
# for i in range(r - 2) :
#     a = i + 1
#     print(a + 0 ,  a + 1 , a + 2)
# print("===============================")

# print("r : " , r)
# for i in range(r - 2) :
#     num = i + 1
#     for j in range(3) : 
#         print(num + j , end=" ")
#     print()

