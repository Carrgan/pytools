import string
from random import choices


def password_gen(symbol=string.punctuation, length=12):
    raw = string.ascii_letters + string.digits + symbol
    return "".join(choices(raw, k=length))
