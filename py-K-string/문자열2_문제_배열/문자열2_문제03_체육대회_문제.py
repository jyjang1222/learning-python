'''
    [문제]
        철수네 반은 체육대회를 준비하고 있다. 
		달리기 리스트는 달리기 대회에 참가하는 학생들이다. 
		배구 리스트는 배구 대회에 참가하는 학생들이다.
		둘 중 하나만 참가하는 학생들을 c리스트에 저장하시오.
	[정답]
		c = ['김철수', '신민아', '최재식', '이진상', '소지석', '유재석', '이민자', '박명수', '유명새', '킬리만자로']
		
'''
달리기 = [
            ["김철수","이서영","최민식"],
            ["조춘자","김말숙","이진상"],
            ["유재석","박명수","킬리만자로"]
        ]
배구 = [
			["신민아","김말숙","최재식"],
			["최민식","이서영","소지석"],
			["이민자","유명새","조춘자"]
	    ]

c = []

run = []
volleyball = []


for i in range(len(달리기)):
	for j in range(len(달리기[i])):
		run.append(달리기[i][j])
		volleyball.append(배구[i][j])

print(run)
print(volleyball)

for i in run:
	chk = True
	for j in volleyball:
		if i == j:
			chk = False
	if chk:
		c.append(i)
for i in volleyball:
	chk = True
	for j in run:
		if i == j:
			chk = False
	if chk:
		c.append(i)
		
print(c)