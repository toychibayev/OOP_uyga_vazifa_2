import os

os.system("cls")

class User:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

def passwords(password: str) -> bool:
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_dot = '.' in password
    return has_lower and has_digit and has_dot

def length(password: str) -> bool:
    return 8 <= len(password) <= 128

while True:
    username = input("Foydalanuvchi nomini kiriting (6-30 belgidan iborat bo'lishi kerak): ")
    if 6 <= len(username) <= 30:
        break
    else:
        raise KeyError("Foydalanuvchi nomi 6 dan 30 gacha bo'lgan belgilarni o'z ichiga olishi kerak.")

while True:
    password = input("Parolni kiriting: ")
    if length(password) and passwords(password):
        break
    else:
        raise KeyError("Parol 8 tadan kam va 128 tadan ko'p bo'lmasligi, kamida bitta kichik harf, raqam va nuqta belgisini o'z ichiga olishi kerak.")

user = User(username, password)
print(f"Foydalanuvchi yaratildi: {user.username}")
