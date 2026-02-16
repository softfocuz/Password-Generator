import random
import string

def password_generator(length=14):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    combinedChars = letters + numbers + symbols

    password = [
        random.choice(letters),
        random.choice(numbers),
        random.choice(symbols)
    ]

    password += [random.choice(combinedChars) for i in range(length - 3)]
    random.shuffle(password)

    return ''.join(password)
