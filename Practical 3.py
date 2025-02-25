numbers = []

for i in range(5):
    num = int(input("Введіть число "))
    numbers.append(num)

print("Найбільше число ", max(numbers))
print("Найменше число ", min(numbers))
