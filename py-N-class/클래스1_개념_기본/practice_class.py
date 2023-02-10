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