'''
	[문제]
		철수는 집에서 학교까지 버스를 타고 다닌다.
		철수의 버스비는 1200원이다. 
		철수는 학교가 끝나면 바로 학원에 간다.
		학원에 갈 때는 지하철을 이용한다.
		지하철 요금은 1100원이다.
		철수가 학원에서 집으로 바로 올 때는 1300원의 차비가 든다.
		철수가 학교에서 집으로 바로 올 때는 1200원의 차비가 든다.
		학교는 월화수목금 매일 다닌다.
		학원은 월수금에만 다닌다.
		이번 달에 철수는 4주 동안 학교와 학원에 다녔다.
		이번 달 필요한 총차비를 구하시오.
		
	[정답] 
		62400
'''

'''
    학교 + 학원
    월수금
    1200 + 1100 + 1300

    학교
    화목
    1200 + 1200
'''

버스_요금 = 1200
지하철_요금 = 1100

학원에서_집 = 1300
학교에서_집 = 1200

월수금 = 버스_요금 + 지하철_요금 + 학원에서_집
화목 = 버스_요금 + 학교에서_집

일주일_비용 = 월수금 * 3 + 화목 * 2
한달_비용 = 일주일_비용 * 4
print(한달_비용)

