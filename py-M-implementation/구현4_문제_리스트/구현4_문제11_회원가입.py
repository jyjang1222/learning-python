"""
	[회원가입] 
		메뉴 => [1.회원가입 2.정보수정 3.회원탈퇴 4.전체출력 0. 종료]
		
 	   	1. 회원가입 = > ID가 있는지 확인하고 없으면 회원가입 한다.
	   	2. 정보수정 = > ID가 있는지 확인하고 있으면 수정한다. 수정은 비밀번호나 이름만 수정할수있다.
	   	3. 삭제 = >  ID가 있는지 확인하고 있으면 삭제
		4. 전체출력 = > 회원 전체 정보를 출력한다. 
"""

member_id = []
member_pw = []
member_name = []
menuList = ['0. 종료', '1. 회원가입', '2. 정보수정', '3. 회원탈퇴', '4. 전체출력']

def printMenu():
    for menu in menuList:
        print(menu)

def join():
    userId = input('아이디를 입력해주세요.\n')
    userPw = input('비밀번호를 입력해주세요.\n')
    userName = input('이름을 입력해주세요.\n')
    member_id.append(userId)
    member_pw.append(userPw)
    member_name.append(userName)

while True:
    printMenu()
    userInput = int(input('메뉴를 입력해주세요.\n'))
    if userInput == 0:
        break
    elif userInput == 1:
        join()
    elif userInput == 4:
        for i in range(len(member_id)):
            pass