import zoneinfo
from datetime import datetime
from zoneinfo import ZoneInfo

dt = datetime(2022, 11, 29, tzinfo=ZoneInfo("Europe/Monaco"))
print(dt)
print(zoneinfo.available_timezones())

print(f'Dzisiaj mamy:', datetime.today())


