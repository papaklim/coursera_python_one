import random

int_list = []

for i in range(10):
    int_list.append(random.randint(0, 20))


def to_str(func):
    str_list = list()
    for i in func:
        str_list.append(str(i))
    return str_list

print(int_list)

print(to_str(int_list))

print("Лямбда: " + str(list(map(lambda x: str(x), int_list))))

