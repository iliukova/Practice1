# 1. Складіть запрошення для гостей з використанням списку.

guests=["Oleg","Egor","Olga"]
print("Dear",guests[0],", I invite you to the celebration!")
print("Dear",guests[1],", I invite you to the celebration!")
print("Dear",guests[2],", I invite you to the celebration!")

# 2. Представте, що комусь з гостей не вийшло прийти та виконайте видалення гостя. Виведіть запрошення для нового списку.

del guests[1]
print(guests)
print("Dear",guests[0],", I invite you to the celebration!")
print("Dear",guests[1],", I invite you to the celebration!")