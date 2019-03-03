import sys

filename = sys.argv[0]
digit_string = sys.argv[1]
print("Имя запущенного файла: " + filename)
if not digit_string.isdigit():
    print("Argument is not digit")
else:
    sum = 0
    for i in digit_string:
        sum = sum + int(i)
    print("Сумма чисел аргумента = " + str(sum))

