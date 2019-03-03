import sys

filename = sys.argv[0]
num_steps = sys.argv[1]
# print("Имя запущенного файла: " + filename)
if not num_steps.isdigit():
    print("Argument is not digit")
else:
    space = ' '
    step = "#"
    count = int(num_steps)
    space_count = count-1
    step_count = count - space_count
    while count > 1:
        stairs = str(space * space_count + step * step_count)
        print(stairs)
        count -= 1
        space_count -= 1
        step_count += 1
    print(step*int(num_steps), end='\r')

