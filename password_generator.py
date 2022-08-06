from random import choices
import string

characters = string.printable[:77]

COMPLEXITY = {
    "1": characters[10:37],
    "2": characters[:37],
    "3": characters[:62],
    "4": characters[:66],
    "5": characters
}

def generate_password():
    no_of_chars = int(input("Please tell me how many characters you want in your password? "))
    difficulty = input("How complex do you want your password? In range of 1 to 5 ")
    if difficulty in COMPLEXITY:
        complex_chars = COMPLEXITY[difficulty]
    else:
        print("Rethink your choices :)")
    password = "".join(choices(complex_chars, k=no_of_chars))
    print(f"Your suggested password is {password}")
    return password

generate_password()