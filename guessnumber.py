import random
_test = 21
print("""
Угадай загаданное число!!!
--------------------------
Для выхода из программы введите \"Exit\" или нажмите Enter с пустым значением.
""")
win_number = random.randint(0,1000)
while True:
    input_number = (input("Введите число: "))
    if input_number == "Exit" or not input_number:
        print("*Вы вышли из программы*")
        break

    if not input_number.isdigit():
        print("Введите корректное значение")
        continue

    if int(input_number) > win_number:
        print("Загаданное число меньше")
    elif int(input_number) < win_number:
        print("Загаданное число больше")
    else:
        print("Верно!")
        break
