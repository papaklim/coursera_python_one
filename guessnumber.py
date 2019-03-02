print("""
Угадай загаданное число!!!
--------------------------
Для выхода из программы введите \"Exit\"
""")
win_number = 99
while True:
    input_number = (input("Введите число: "))
    if input_number == "Exit" or not input_number:
        print("Вы вышли из программы")
        break
    elif int(input_number) > win_number:
        print("Загаданное число меньше")
    elif int(input_number) < win_number:
        print("Загаданное число больше")
    else:
        print("Верно!")
        break
