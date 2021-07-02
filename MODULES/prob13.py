# Определить дату, которая наступит через 1000 дней от текущей даты

import datetime

dt = datetime.datetime.now()
thdt = datetime.timedelta(days=1000)
result = dt+thdt
print(result)