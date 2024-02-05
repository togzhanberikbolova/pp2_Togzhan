def prime( k ):
    if k == 0:
        return True
    else:
        for i in range(2, k // 2+1 ):
            if k % i == 0:
                return False
    return True
def filter_prime(list):
    primes = []
    for i in range(len(list)):
        if prime(list[i]):
            primes.append(list[i])
    return primes
print(filter_prime([1,2,3,4,5,6,7,8,9,10]))