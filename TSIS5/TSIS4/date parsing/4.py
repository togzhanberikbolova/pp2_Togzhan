from datetime import datetime, timedelta

dt1 = datetime.today()
dt2 = datetime.today() + timedelta(1)

timedelta = dt2 - dt1
x = timedelta.days * 24 * 3600 + timedelta.seconds
print(x)

