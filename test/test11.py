import random
# 1
arr = [
"권종률" , "김식" , "김유정" , 
"김지현" , "송민수" , "신정규" ,
"안성현" , "안지선" , "양나비" ,
"유재형" , "이주호" , "장준영" , 
"황지현" , "김사라" , "이근일"]

a = []
b = []
c = []
d = []
e = []

def team(teamName):
    rarr = []
    while True:
        if len(rarr) == 3:
            break
        chk = True
        r = random.randint(0, len(arr) - 1)
        for i in range(len(rarr)):
            if rarr[i] == arr[r]:
                chk = False
        if chk:
            rarr.append(arr[r])
    for i in range(len(rarr)):
        teamName.append(rarr[i])
        arr.remove(rarr[i])
    return teamName

print(team(a))
print(team(b))
print(team(c))
print(team(d))
print(team(e))


