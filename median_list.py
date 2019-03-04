import random

rnd_list = []

for _ in range(random.randint(10, 15)):
    rnd_list.append(random.randint(1, 20))
rnd_list.sort()
print(rnd_list)

median = None
half_size = len(rnd_list) // 2
if half_size % 2 == 1:
    median = rnd_list[half_size]
else:
    median = sum(rnd_list[half_size -1 : half_size + 1]) / 2


print(half_size)
print(median)

