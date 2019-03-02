win_number = 99
while True:
    input_number = int(input("Введите число: "))
    if input_number > win_number:
        print("Загаданное число меньше")
    elif input_number < win_number:
        print("Загаданное число больше")
    else:
        print("Верно!")
        break