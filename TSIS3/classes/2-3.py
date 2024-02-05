#2
class Shape:
    def area(self):
        self.a=0
        print(self.a)
class Square(Shape):
    def __init__(self):
        self.length=int(input("length: "))
    def area(self):
        self.a=self.length*self.length
        print(self.a)
x=Square()
x.area()
#3
class Rectangle(Shape):
    def __init__(self):
        self.lengthR=int(input("length: "))
        self.widthR=int(input("width: "))
    def areaR(self):
        self.a=self.lengthR*self.widthR
        print(self.a)  
x=Rectangle()
x.areaR()
