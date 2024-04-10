import math
sides = int(input("Input number of sides: "))
length = int(input("Input length of a side: "))
if sides == 3:
    area = (math.sqrt(3)/4) * (length)**2
elif sides == 4:
    area = length ** 2
elif sides == 5:
    area = 0.25 * (length)**2 * (math.sqrt(5*(5+2*math.sqrt(5))))
elif sides == 6:
    area = (3*math.sqrt(3)/2)*length**2
elif sides == 7:
    area = (7/5) * length**2 * (math.cos(180/7))
elif sides == 8:
    area = 2*length**2*(1+math.sqrt(2))
print("The area of polygon is: ", area)
    