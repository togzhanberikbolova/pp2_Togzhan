def isPalindrome(s):
    return s == s[::-1]

s = input("Enter s: ")
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")