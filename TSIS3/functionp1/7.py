def has_33( n ) :
    cnt = 0
    for i in n:
        if i == 3:
            cnt+=1
        else:
            cnt = 0
        if cnt == 2:
            return True
    return False

print(has_33([1,3,3]))
            