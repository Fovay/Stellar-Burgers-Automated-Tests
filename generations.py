import random
import string

URL = 'https://stellarburgers.education-services.ru/'
Test_name = 'Анастасия'
Test_email = 'grafova_anastasiya_47@yandex.ru'
Test_password = '123456'

def generate_email():
    return (f"grafova_anastasiya_47_"f"{random.randint(100, 999)}@yandex.ru")

def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))