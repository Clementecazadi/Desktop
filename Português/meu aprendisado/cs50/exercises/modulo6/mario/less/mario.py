from cs50 import get_int

global height
height = get_int("Height: ")
while 0 >= height or height > 8:
    height = get_int("Height: ")

def drawn(h= 1):
    if h > 1:
        drawn(h - 1)
    for c in range(height, 0, -1):
        if c > h:
            print(' ', end='')
            continue
        print('#', end='')
    print()
drawn(height)
