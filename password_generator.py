import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = "!@#$%&*()<>{}[]?=+"

def generate_password(length=8):
    printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'

    printable = list(printable)
    random.shuffle(printable)

    password = random.choices(printable, k=length)
    password = ''.join(password)

    return password