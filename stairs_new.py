import sys

num_steps = int(sys.argv[1])

i = 0
while i < (num_steps-1):
    i += 1
    print(" " * (num_steps - i), "#"*i, sep='')
print('#'*num_steps, end='\r')
