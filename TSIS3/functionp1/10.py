def uni(lst):
    check = []
    for i in lst:
        if i not in check:
            check.append(i)
    return check   