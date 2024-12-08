from datetime import datetime, timedelta

DAYS_NUM = 30

current = datetime.now()
future_date = current + timedelta(days=DAYS_NUM)
formatted_date = future_date.strftime('%Y-%m-%d')

print(f'Через {DAYS_NUM} дней будет: {formatted_date}')