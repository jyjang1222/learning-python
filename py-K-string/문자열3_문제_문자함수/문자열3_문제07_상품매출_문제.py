'''
    [문제]
        member는 회원목록이다. 번호와 아이디가 기록되어있다.
        item은 쇼핑몰 판매상품이다. 상품이름과 가격이 기록되어있다.
        
        order는 오늘 주문 목록이다. 주문한회원아이디와 아이템이름 그리고, 주문개수가 기록되어있다. 
        오늘의 매출을 출력하시오.
    
    [정답]
        33200
'''

member = "qwer1234,pythongood,testid"
item = "사과,1100/바나나,2000/딸기,4300"
order = "qwer1234,사과,3/phthongood,바나나,2/qwer1234,딸기,5/testid,사과,4"

member = member.split(',')
item = item.split('/')
order = order.split('/')

itemArr = []
for i in item:
    tmp = i.split(',')
    itemArr.append(tmp)

orderArr = []
for i in order:
    tmp = i.split(',')
    orderArr.append(tmp)

print(member)
print(itemArr)
print(orderArr)

total = 0
for i in range(len(orderArr)):
    for j in range(len(itemArr)):
        if orderArr[i][1] == itemArr[j][0]:
            calc = int(itemArr[j][1]) * int(orderArr[i][2])
            total += calc
            break
print(total)
