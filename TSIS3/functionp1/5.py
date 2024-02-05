import itertools
def permut( string ):
    lst = list( itertools.permutations( string ) )
    for tup in lst:
        print(''.join(tup))