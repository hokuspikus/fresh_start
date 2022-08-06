from random import choices
import string

characters = string.printable[:95]

def generate_password():
    no_of_chars = int(input("Please tell me how many characters you want in your password? "))
    password = "".join(choices(characters, k=no_of_chars))
    print(f"Your suggested password is {password}")
    return password

generate_password()