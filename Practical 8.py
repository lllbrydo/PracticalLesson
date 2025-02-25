import re




def isvalid(phone):
    pattern = r'^\+380\d{9}$'
    if re.match(pattern, phone):
        print("валідний")
    else:
        print("невалідний")

phone = input("введіть номер ")
isvalid(phone)
