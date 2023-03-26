import re


while True:
    email = input("What's your email? ").strip()

    if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.\w{1,3}$", email, flags=re.IGNORECASE):
        print("Valid")
    else:
        print("Invalid")
