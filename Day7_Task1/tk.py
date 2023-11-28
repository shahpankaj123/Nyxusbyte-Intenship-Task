from datetime import date

today = date.today()
formatted_date = today.strftime('%B %d, %Y')
print(formatted_date)
print(today)