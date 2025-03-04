import datetime


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

class Cart:
    def __init__(self):
        self.products = []

    # додаємо товар до кошика
    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} додано!")

    # видаляємо із кошика товар
    def remove_product(self, product_name):
     try:
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"{product_name} видалено")
                return
            print("товар не знайдено")
     except Exception as problem:
            print(f"помилка {problem}")

    #  загальна сума в кошику
    def get_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def show_cart(self):
     try:
        if not self.products:
            print("в кошику нічого немає")
        else:
            print("ваш кошик:")
            for product in self.products:
                print(f"{product.name} {product.price} грн")
     except Exception as problem:
         print(f"помилка {problem}")

products = [
    Product("test", 1000, "test"),
    Product("Iphone 16 Pro Max", 65000, "Електрика"),
    Product("Apple iPad 11", 25000, "Електрика"),
    Product("Samsung 111111", 10500, "Електрика"),
    Product("Samsung 12222", 21500, "Електрика")
]

cart = Cart()

while True:
    print("1 - додати товар в кошик")
    print("2 - видалити товар із кошика")
    print("3 - показати кошик")
    print("4 - оформити замовлення")

    try:
        choice = input("виберіть ")

        if choice == "1":
            print("товари")
            for product in products:
                print(f"{product.name} ({product.category}) {product.price} грн")
            name = input("виберіть товар: ")

            naideno = None
            for product in products:
                if product.name == name:
                    naideno = product
                    break

            if naideno:
                cart.add_product(naideno)
            else:
                print("не зднайдено")

        elif choice == "2":
            name = input("введіть товар для видалення ")
            cart.remove_product(name)

        elif choice == "3":
            cart.show_cart()

        elif choice == "4":
            total = cart.get_total()
            print(f"загальна сума {total} грн")
            confirm = input("оформити замовлення (Так/Ні) ")
            if confirm == "Так":
                zakaz_day = datetime.date.today()
                print(f"Замовлення оформлено на {zakaz_day}")
                print("оформлено")
                cart = Cart()
            else:
                print("скасовано")

    except Exception as problem:
        print(f"помилка {problem}")