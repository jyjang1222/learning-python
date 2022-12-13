"""
	[쇼핑몰]
		쇼핑몰을 구현하려고한다.
		쇼핑몰의 메인카테고리는 [1.남성의류][2.여성의류][0.종료] 이며,
		남성의류를 선택한경우 [1.티셔츠][2.바지][0.뒤로가기]의 새로운 메뉴가 나온다.
		뒤로가기를 고르기 전까지 세부항목이 계속 보여기제되며, 뒤로가기를 선택하면
		메인카테고리가 다시보여진다.
		세부항목은 아래와 같다.
	[예시]
		1. 남성의류
	 		1. 티셔츠
	 		2. 바지
	 		0. 뒤로가기
	 	2. 여성의류
	 		1. 가디건
	 		2. 치마
	 		0. 뒤로가기
		0. 종료
"""

category = [{'cloth':'남성의류'}, {'cloth':'여성의류'}]
man = [{'남성의류': '티셔츠'}, {'남성의류': '바지'}]
woman = [{'여성의류': '가디건'}, {'여성의류': '치마'}]

while True:
	for i in category:
		print(i)
	select = int(input('[1.남성의류][2.여성의류][0.종료]\n'))
	if select == 1:
		for j in man:
			print(j)
		select2 = int(input('[0.뒤로가기]\n'))
		if select2 == 0:
			continue
	if select == 2:
		for j in woman:
			print(j)
		select2 = int(input('[0.뒤로가기]\n'))
		if select2 == 0:
			continue
	if select == 0:
		break