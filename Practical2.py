sprav = input("Введіть список справ через кому  ").split(",")

while sprav:
    print("Ваші справи ")
    for i in range(len(sprav)):
        print(f"{i+1} {sprav[i]}")

    choice = input("Введіть номер справи щоб видалити ")

    if choice.isdigit() and 1 <= int(choice) <= len(sprav):
        sprav.pop(int(choice) - 1)
    else:
        print("еррор!")

