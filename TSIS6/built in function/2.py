
def calculate(string):
    upper_count=sum(1 for char in string if char.isupper())
    lower_count=sum(1 for char in string if char.islower())
    return upper_count, lower_count
string="HI, How are you?"
upper_count, lower_count=calculate(string)
print("uppercase letter: ", upper_count)
print("lowercase letter: ", lower_count)
