name = input("Імя ")
stavka = float(input("Ставка за годину "))
hours = int(input("Відпрацьовані години "))

salary = stavka * hours * 0.8
print(f"{name} ваша зарплата {salary}")
