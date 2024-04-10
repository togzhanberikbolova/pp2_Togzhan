def Divisible(n):
    if n<0:
        return ValueError("Error")
    for i in range(n+1):
        if i%3 == 0:
            yield i
        elif i%4 == 0:
            yield i

n = int(input("Enter n: "))
for div in Divisible(n):
    print(div)