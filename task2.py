import locale
locale.setlocale(locale.LC_TIME, 'ru_RU')

from datetime import datetime

current = datetime.now()

date = current.strftime('%Y-%m-%d %H:%M:%S')
week_day = current.strftime('%A').title()
week_num = current.isocalendar()[1]

print(f'День и время: {date}')
print(f'День недели: {week_day}')
print(f'Номер недели: {week_num}')
