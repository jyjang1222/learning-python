'''
[키오스크]
	철수는 햄버거 가게를 운영한다.
	가게 내에 키오스크를 설치하고 잘 작동하는지 테스트하고 있다.
	랜덤으로 번호를 선택하고 아이템과 현금을 비교 후 결과를 출력하시오.

	해당 상품 가격이 현금보다 적으면, 현금에서 차감하고 구입 메세지를 출력하시오.
	해당 상품 가격이 현금보다 클 경우, "구입불가" 메세지를 출력하시오.
'''
import random

# 현금 = 3000
# 메뉴1 = 2500
# 메뉴2 = 3500

# 메뉴 출력
# print("[키오스크]")
# print("[1] 햄버거 2500원")
# print("[2] 치킨조각 3500원")

# 번호 선택
# print("번호를 입력하세요 : ")
# select = random.randint(1, 2)
# print("번호" , select , "을/를 선택하셨습니다.")

# 결과 출력
# if select == 1:
# 	if 현금 >= 메뉴1:
# 		print("햄버거를 구입합니다.")
# 		현금 = 현금 - 메뉴1
# 		print("남은금액 : " , 현금)
# 	if 현금 < 메뉴1:
# 		print("구입불가.")

# if select == 2:
# 	if 현금 >= 메뉴2:
# 		print("치킨버거를 구입합니다.")
# 		현금 = 현금 - 메뉴2
# 		print("남은금액 : " , 현금)
# 	if 현금 < 메뉴2:
# 		print("구입불가.") 

# print("-----------------------")

# 중첩 if문을 사용하지 않았을 때
# if select == 1 and 현금 >= 메뉴1:
# 	print("햄버거를 구입합니다.")
# 	현금 = 현금 - 메뉴1
# 	print("남은금액 : " , 현금)
# if select == 1 and 현금 < 메뉴1:
# 	print("구입불가.")

# if select == 2 and 현금 >= 메뉴2:
# 	print("치킨버거를 구입합니다.")
# 	현금 = 현금 - 메뉴2
# 	print("남은금액 : " , 현금)
# if select == 2 and 현금 < 메뉴2:
# 	print("구입불가.") 

# 내문제풀이 -1차
print("-----------------------")
money = random.randint(1000, 10000)
wapper = random.randint(1000, 5000)
bigmac = random.randint(1000, 5000)
rand = random.randint(1, 2)

print("1. 와퍼:", wapper, "원", "2. 빅맥:", bigmac, "원 현금:", money)
if rand == 1:
	print("와퍼를 선택하셨습니다.")
	if wapper > money:
		print("현금이", wapper - money , "원 부족합니다.")
	if wapper <= money:
		money -= wapper
	print("와퍼구입완료. 현재 현금:", money)
if rand == 2:
	print("빅맥을 선택하셨습니다.")
	if bigmac > money:
		print("현금이", bigmac - money, "원 부족합니다.")
	if bigmac <= money:
		money -= bigmac
		print("빅맥구입완료. 현재 현금:", money)