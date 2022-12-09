'''
    [문제]
        itemList은 쇼핑몰 판매상품데이터이다.
        itemName 는 상품이름이다.
        price는 아이템 가격이다.
        
        orderList는 오늘 주문 목록이다. 
        ordernumber 는 주문번호이다. 
        orderid 는 주문한 회원 id 이다.
        itemName 는 주문한 상품이름이다. 
        count 는 주문한 상품개수이다. 

        cancelList 는 주문취소 목록이다. 
        cancelnumber 는 주문을 취소한 번호이다. 

        취소한 상품이름별 총가격을 구하는 함수를 만드시오.
        
    [정답]   
        [{'itemname': '바나나', 'total': 22000}, {'itemname': '딸기', 'total': 25800}]
'''

itemList = [
    {"itemname" : "사과" , "price" : 1100},
    {"itemname" : "바나나" , "price" : 2000},
    {"itemname" : "딸기" , "price" : 4300},
]
orderList = [
    {"ordernumber" : 100001 , "orderid" : "qwer1234" , "itemname" : "사과" , "count" : 3},
    {"ordernumber" : 100002 , "orderid" : "pythongood" , "itemname" : "딸기" , "count" : 6},
    {"ordernumber" : 100003 , "orderid" : "testid" , "itemname" : "바나나" , "count" : 4},
    {"ordernumber" : 100004 , "orderid" : "pythongood" , "itemname" : "사과" , "count" : 2},
    {"ordernumber" : 100005 , "orderid" : "testid" , "itemname" : "바나나" , "count" : 7},
    {"ordernumber" : 100006 , "orderid" : "qwer1234" , "itemname" : "사과" , "count" : 2}, 
    {"ordernumber" : 100007 , "orderid" : "testid" , "itemname" : "사과" , "count" : 3}, 
]
cancelList = [
    {"cancelnumber" : 100003 },
    {"cancelnumber" : 100002 },
    {"cancelnumber" : 100005 },
]

totalList = []

def combineOrderCancelInfo(orderDictList, cancelDictList):
    tmp = []
    for i in cancelDictList:
        dict = {}
        for j in orderDictList:
            cancelNumber = i['cancelnumber']
            orderNumber = j['ordernumber']
            if cancelNumber == orderNumber:
                dict['itemname'] = j['itemname']
                dict['count'] = j['count']
        tmp.append(dict)
    return tmp

cancelList = combineOrderCancelInfo(orderList, cancelList)

for i in cancelList:
    print(i)

# 중복데이터 합치기
def combineDuplicatedData(dictList):
    tmp = []
    for i in dictList:
        chk = True
        for j in tmp:
            if j['itemname'] == i['itemname']:
                chk = False
                j['count'] += i['count']
        if chk:
            tmp.append(i)
    return tmp

cancelList = combineDuplicatedData(cancelList)

for i in cancelList:
    print(i)

def getTotalList(data, itemDictList):
    tmp = []
    for i in data:
        dict = {}
        for j in itemDictList:
            if i['itemname'] == j['itemname']:
                calc = i['count'] * j['price']
                dict['itemname'] = i['itemname']
                dict['total'] = calc
        tmp.append(dict)
    return tmp

cancelList = getTotalList(cancelList, itemList)

for i in cancelList:
    print(i)
