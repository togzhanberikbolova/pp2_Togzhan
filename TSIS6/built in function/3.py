def polindrome(string):
    string=string.replace(" ","").lower()
    return string==string[::-1]
string1="Pop"
string2="hi"
print(polindrome(string1))
print(polindrome(string2))