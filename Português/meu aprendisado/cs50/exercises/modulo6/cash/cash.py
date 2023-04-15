from cs50 import get_float
from math import floor

def main():
    money = get_pos_float("Change owed: ")
    print(f"{cash(money)}")


def get_pos_float(text:str) -> float:
    height = get_float(text)
    while 0.00 >= height or height > 100.00:
        height = get_float(text)
    return floor(height * 100)


def cash(money:float) -> int:
    count = 0
    while money > 0:
        if money >= 25:
            money -= 25

        elif money >= 10:
            money -= 10

        elif money >= 5:
            money -= 5

        elif money >= 1:
            money -= 1
        count += 1
    return count

main()
