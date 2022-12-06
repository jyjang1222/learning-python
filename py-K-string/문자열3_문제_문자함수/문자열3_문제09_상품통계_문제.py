'''
    [문제]
        member는 회원목록이다.
        item은 쇼핑몰 판매상품이다.
        order는 오늘 주문목록이다.
        회원별 아이템 주문개수를 출력하시오.
    [정답]
        이만수: 고래밥 3
        김철민: 고래밥 1 칸쵸 1
        이영희: 새우깡 2 칸쵸 1
'''

member  = "3001/이만수,3002/김철민,3003/이영희"
item    = "1001/고래밥,1002/새우깡,1003/칸쵸"
order   = "3001,1001/3001,1001/3003,1002/3002,1003/3001,1001/3003,1002/3003,1003/3002,1001"

member = member.split(',')
item = item.split(',')
order = order.split('/')

def separate(chr, arr):
    emptyArr = []
    for i in arr:
        tmp = i.split(chr)
        emptyArr.append(tmp)
    return emptyArr

memberArr = separate('/', member)
itemArr = separate('/', item)
orderArr = separate(',', order)

# print(memberArr)
# print(itemArr)
# print(orderArr)

# 1
for i in range(len(memberArr)):
    tmp2 = []
    for j in range(len(itemArr)):
        tmp = []
        cnt = 0
        for k in range(len(orderArr)):
            # 아이템목록과 과자종류 같은지
            if itemArr[j][0] == orderArr[k][1]:
                # 현재멤버와 주문멤버 같은지
                if memberArr[i][0] == orderArr[k][0]:
                    cnt += 1
        tmp.append(itemArr[j][1])
        tmp.append(cnt)
        tmp2.append(tmp)    
    print(memberArr[i][1], tmp2)


# 2
tmp2 = []
for i in range(len(memberArr)):
    tmp = []
    for j in range(len(itemArr)):
        cnt = 0
        for k in range(len(orderArr)):
            # 아이템목록과 과자종류 같은지
            if itemArr[j][0] == orderArr[k][1]:
                # 현재멤버와 주문멤버 같은지
                if memberArr[i][0] == orderArr[k][0]:
                    cnt += 1
        tmp.append(cnt)
    tmp2.append(tmp)    
print(tmp2)


for j in range(len(tmp2)):
    print(memberArr[j][1], end = " ")
    for k in range(len(tmp2[j])):
        if tmp2[j][k] != 0:
            print(itemArr[k][1], tmp2[j][k], end = " ")
    print()
