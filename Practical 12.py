def convert(amount, course):
    return amount / course

uah = float(input("Скільки у вас гривень: "))

valuta = input("У яку валюту ви хочете конвертувати ")

kursy = {"USDT": 41.2, "EUR": 44.3}

if valuta in kursy:
    print(f"{convert(uah, kursy[valuta])} {valuta}")
else:
    print("Помилка")
