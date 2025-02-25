contacts = {
    "Назар":"+1801203210",
    "Ігор":"+38012312151"
}



def display_contacts():
    if contacts:
        print("список контактів ")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("контактів поки немає")


def add_contact():
    name = input("введіть імя контакту: ")
    phone = input("введіть номер телефону: ")
    if name in contacts:
        print(f"контакт з імям {name} є")
    else:
        contacts[name] = phone
        print(f"контакт {name} з номером {phone} додано")


def search_contact():
    name = input("введіть ія для пошуку: ")
    if name in contacts:
        print(f"контакт знайдено: {name} - {contacts[name]}")
    else:
        print(f"контакт з імям {name} не знайдено")


def main_menu():
    while True:
        print("менюшка")
        print("(1) показати всі контакти")
        print("(2) додати новий контакт")
        print("(3) знайти контакт")
        print("(4) вийти")

        choice = input("варіант:")

        if choice == "1":
            display_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("зупинка.............")
            break
        else:
            print("неправильно")


main_menu()
