import math
import time
def square(number, milisecond):
    time.sleep(milisecond/1000)
    result=math.sqrt(number)
    print(f"Square root of {number} after {milisecond} miliseconds is {result}")
number=25100
milisecond=2123
square(number, milisecond)