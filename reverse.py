import string
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))
id_generator()

def reverse(text):
    text = [text]
    for i in reversed(text):
        return i[::]
    return

