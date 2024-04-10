def SquareNum(a,b):
    if a<0 and b<0 :
        return ValueError("Error")
    for i in range(a,b+1):
        yield i**2

a = int(input("Enter a: "))
b = int(input("Enter b: "))
for square in SquareNum(a,b):
    print(square)