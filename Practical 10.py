import datetime

def newyear():
    today = datetime.date.today()
    next_new_year = datetime.date(year=today.year + 1, month=1, day=1)
    return (next_new_year - today).days

ostalos = newyear()
print(f"до наступного Нового року залишилося {ostalos} днів.")

def age(birth_date):
    today = datetime.date.today()
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        months -= 1
        days += 30

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

birth_date = datetime.date(2003, 12, 23)
years, months, days = age(birth_date)
print(f"вам {years} років {months} місяців {days} днів")