def spy_game( n ):
    check = ''
    for i in n:
        check += str(i)
    if '007' in check:
        print( True )
    else:
        print( False )
spy_game([1,0,0,8])
spy_game([0,0,7,2])