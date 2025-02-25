class Car:
    def __init__(self, marka, model, rik, probig):
        self.marka = marka
        self.model = model
        self.rik = rik
        self.probig = probig

    def __str__(self):
        return f"{self.rik} {self.marka} {self.model}, пробіг: {self.probig} км"

class Owner:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def show_cars(self):
        if self.cars:
            print(f"{self.name} має машини")
            for car in self.cars:
                print(car)
        else:
            print(f"{self.name} немає машин")

    def add_car(self, car):
        self.cars.append(car)


car1 = Car("bmw", "X5", 2020, 115700)
car2 = Car("mercedes", "S-Class", 2024, 3500)
car3 = Car("bmw", "X6", 2019, 145700)


owner1 = Owner("nazar")
owner1.add_car(car1)
owner1.add_car(car3)
owner1.show_cars()


owner2 = Owner("vanya")
owner2.add_car(car2)
owner2.show_cars()
