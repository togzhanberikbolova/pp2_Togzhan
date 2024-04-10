def Return(n):
    if n<0:
        return ValueError("Error")
    for i in range (n+1):
        yield n-i

n = int(input("Enter n: "))
for x in Return(n):
    print(x)