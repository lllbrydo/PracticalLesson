import re




def isvalid(email):
    pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.(com)$'
    if re.match(pattern, email):
        print("валідна")
    else:
        print("невалідна")

email = input("введіть електронну пошту ")
isvalid(email)
