import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = "!@#$%&*()<>{}[]?=+"

def generate_password(length=8):
    printable = f'{LETTERS}{NUMBERS}'

    printable = list(printable)
    random.shuffle(printable)

    password = random.choices(printable, k=length)

    for i in range(random.randint(1,2)):
        pos = random.randint(0,length-1)
        x = PUNCTUATION[random.randint(0,17)]
        password[pos] = x

    password = ''.join(password)

    return password