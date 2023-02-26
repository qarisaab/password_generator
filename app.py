import string
import random

def generate_password(min_length, numbers=True, special_character=True):
    letters= string.ascii_letters
    number = string.digits
    special = string.punctuation

    characters = letters

    if number:
        characters += number

    if special:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in number:
            has_number = True

        if new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_character:
            meets_criteria = meets_criteria and has_special


    return pwd

pwd=generate_password(int(input("Enter the length of the password: " )))
print(pwd)

