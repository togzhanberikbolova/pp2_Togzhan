def SquareNum(N):
    if N<0:
        return ValueError("Error")
    for i in range(N+1):
        yield i**2
    
N = int(input("Input n: "))
for square in SquareNum(N):
    print(square)
