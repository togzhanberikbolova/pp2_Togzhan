def EvenNum(n):
    if n<0:
        return ValueError("Error")
    for i in range(n+1):
        if i%2 == 0:
            yield i

n = int(input("Enter n : "))
for even in EvenNum(n):
    print(even)