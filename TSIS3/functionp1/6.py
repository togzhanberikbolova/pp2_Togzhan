def reverse( word ) :
    lst = word.split()
    lst = lst[ -1 :: -1 ]
    print( lst )
    
reverse(str(input("Enter word: ")))