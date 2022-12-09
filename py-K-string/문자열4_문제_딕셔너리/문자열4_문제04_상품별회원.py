'''
    [문제]
        memberList는 회원목록데이터이다.
        number 는 회원 번호이다. 
        id 는 회원아이디이다.

        itemList은 쇼핑몰 판매상품데이터이다.
        itemname 는 상품이름이다.
        price는 아이템 가격이다.
        
        orderList는 오늘 주문 목록이다. 
        orderid 는 주문한 회원 id 이다.
        itemname 는 주문한 상품이름이다. 
        count 는 주문한 상품개수이다. 

        각회원별 상품별 이름과 총가격을 구하시오.
        단, 아무것도 주문하지않은 회원은 구하지않는다.
    [정답]
        {'orderid': 'qwer1234', 'itemname': '사과', 'count': 4, 'total': 4400}
        {'orderid': 'pythongood', 'itemname': '딸기', 'count': 6, 'total': 25800}
        {'orderid': 'testid', 'itemname': '바나나', 'count': 8, 'total': 16000}
        {'orderid': 'pythongood', 'itemname': '사과', 'count': 2, 'total': 2200}
        {'orderid': 'cccddd', 'itemname': '바나나', 'count': 3, 'total': 6000}
        {'orderid': 'cccddd', 'itemname': '사과', 'count': 2, 'total': 2200}
'''
memberList = [
    {"number" : 1001 , "id" : "qwer1234" },
    {"number" : 1002 , "id" : "pythongood"},
    {"number" : 1003 , "id" : "testid"},
    {"number" : 1004 , "id" : "aaabbb"},
    {"number" : 1005 , "id" : "cccddd"},
]
itemList = [
    {"itemname" : "사과" , "price" : 1100},
    {"itemname" : "바나나" , "price" : 2000},
    {"itemname" : "딸기" , "price" : 4300},
]
orderList = [
    {"orderid" : "qwer1234" , "itemname" : "사과" , "count" : 3},
    {"orderid" : "pythongood" , "itemname" : "딸기" , "count" : 6},
    {"orderid" : "testid" , "itemname" : "바나나" , "count" : 1},
    {"orderid" : "pythongood" , "itemname" : "사과" , "count" : 2},
    {"orderid" : "testid" , "itemname" : "바나나" , "count" : 7},
    {"orderid" : "qwer1234" , "itemname" : "사과" , "count" : 1}, 
    {"orderid" : "cccddd" , "itemname" : "바나나" , "count" : 3},
    {"orderid" : "cccddd" , "itemname" : "사과" , "count" : 2},
]

tmp = []
# orderList 중복합치기
for i in range(len(orderList)):
    chk = True
    # 넣을값이 이미 tmp에 있다면 false
    for j in range(len(tmp)):
        if orderList[i]['orderid'] == tmp[j]['orderid']:
            if orderList[i]['itemname'] == tmp[j]['itemname']:
                chk = False
                tmp[j]['count'] += orderList[i]['count']
    if chk:
        tmp.append(orderList[i])

orderList = tmp

# for i in orderList:
#     print(i)

for i in range(len(orderList)):
    for j in range(len(itemList)):
        if orderList[i]['itemname'] == itemList[j]['itemname']:
            total = itemList[j]['price'] * orderList[i]['count']
            orderList[i]['total'] = total

for i in orderList:
    print(i)

