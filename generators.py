import random
import string

def generate_email():
    return f"grafova_anastasiya_47_{random.randint(100,999)}@yandex.ru"

def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))