import calendar
from datetime import datetime

today = datetime.today()
last_day = calendar.monthrange(today.year, today.month)[1]
seconds = last_day * 24 * 60 * 60
print(seconds)
