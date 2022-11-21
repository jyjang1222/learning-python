'''
	[문제]
		아래와 같이 출력하시오.
'''
'''
	[문제1]
		11112
		11122
		11222
		12222
'''
print("[문제1]")

for i in range(1, 5):
	for j in range(5 - i):
		print("1", end = "")
	for k in range(i):
		print("2", end = "")
	print()


'''
	[문제2]
		12222
		11222
		11122
		11112
'''
print("[문제2]")

for i in range(1, 5):
	for j in range(i):
		print("1", end = "")
	for k in range(5 - i):
		print("2", end = "")
	print()

'''
	[문제3]
		11211
		12221	
		22222
'''
print("[문제3]")

for i in range(1, 4):
	for j in range(3 - i):
		print("1", end = "")
	for j in range(2 * i - 1):
		print("2", end = "")
	for j in range(3 - i):
		print("1", end = "")
	print()

'''
	[문제4]
		  2
		 222
		22222
'''
print("[문제4]")

for i in range(1, 4):
	for j in range(3 - i):
		print(" ", end = "")
	for j in range(2 * i - 1):
		print("2", end = "")
	for j in range(3 - i):
		print(" ", end = "")
	print()

'''
	[문제5]
		22222
		 222
		  2   
'''
print("[문제5]")

for i in range(3, 0, -1):
	for j in range(3 - i):
		print(" ", end = "")
	for j in range(2 * i - 1):
		print("2", end = "")
	for j in range(3 - i):
		print(" ", end = "")
	print()



