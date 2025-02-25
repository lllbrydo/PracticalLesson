slovnik = {
    "Hello": "Привіт",
    "Goodbye": "До побачення",
    "Please": "Будь ласка",
    "Yes": "Так",
    "No": "Ні",
    "hello": "Привіт",
    "goodbye": "До побачення",
    "please": "Будь ласка",
    "yes": "Так",
    "no": "Ні"

}

def perekladslova():
    word = input("введіть слово ( на англійській мові ) ")
    pereklad = slovnik.get(word)
    if pereklad:
        print(f"Переклад - {pereklad}")
    else:
        print("помилка")

perekladslova()
