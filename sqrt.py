import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = int(b) ** 2 - 4 * int(a) * int(c)

print("D = " + str(d))
if d < 0:
    print("Уравнение не имеет квадратных корней")
elif d == 0:  # например a = 1, b = 6, c = 9
    x = int(-int(b)/2*int(a))
    print("Уравнение имеет 1 квадратный корень x = " + str(x))
else:
    x1 = int((-int(b) + d ** 0.5)/2)
    x2 = int((-int(b) - d ** 0.5)/2)
    print("Уравнение имеет 2 квадратных корня x1 = " + str(x1) + "; x2 = " + str(x2))
