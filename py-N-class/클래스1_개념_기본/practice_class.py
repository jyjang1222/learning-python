class Cat:
    name = ''
    age = 0
    color = ''
    def printInfo(self):
        print(self.name, self.age, self.color)
    def cry(self):
        print(self.name, ': 야옹 ~')

cat1 = Cat()
cat1.name = 'myCat1'
cat1.age = 1
cat1.color = 'black'
cat1.printInfo()
cat1.cry()

# 생성자 연습
class Dog:
    def __init__(self, a, b, c):
        self.name = a
        self.age = b
        self.color = c
    def printInfo(self):
        print(self.name, self.age, self.color)
    def cry(self):
        print(self.name, ': 멍멍 !')

dog1 = Dog('myDog1', 1, 'brown')
dog1.printInfo()
dog1.cry()
# dog2 = Dog() -> 에러발생

# 상속연습
class Animal:
    def __init__(self, a, b, c):
        self.name = a
        self.age = b
        self.color = c
    def printInfo(self):
        print(self.name, self.age, self.color)
class Owl(Animal):
    def cry(self):
        print(self.name, ': 부엉 ~')
class Wolf(Animal):
    def cry(self):
        print(self.name, ': 아우 ~')

owl1 = Owl('myOwl1', 2, 'white')
owl1.printInfo()
owl1.cry()
wolf1 = Wolf('myWolf1', 3, 'gray')
wolf1.printInfo()
wolf1.cry()
