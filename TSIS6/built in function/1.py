from functools import reduce
def multiply(numbers):
    result = reduce(lambda x,y:x*y, numbers)
    return result

numbers=[1,2,3,4,5]
print(multiply(numbers))
    

