from datetime import date, timedelta

y = date.today() - timedelta(1)
t = date.today() + timedelta(1)
print("Today: " , date.today())
print("Yesterday: " , y)
print("Tomorrow: " , t)