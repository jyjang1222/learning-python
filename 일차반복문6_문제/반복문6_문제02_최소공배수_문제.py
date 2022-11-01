'''
[문제] 
	45와 60, 75의 최소공배수를 구하시오.
[정답]
	900
'''

i = 0

while True:
	i += 45
	if i % 60 == 0 and i % 75 == 0:
		print(i)
		break