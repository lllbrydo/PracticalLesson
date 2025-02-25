import random

def guess_number():
    random_number = random.randint(1, 100)
    user_guess = 0
    sprob = 5

    print("Угадай число від 1 до 100")

    while user_guess != random_number and sprob > 0:
        user_guess = int(input(f"Введіть ваше число у вас є {sprob} спроб "))
        sprob -= 1

        if user_guess < random_number:
            print("Більше")
        elif user_guess > random_number:
            print("Менше")
        else:
            print("Угадав!!!!!!!")

guess_number()
