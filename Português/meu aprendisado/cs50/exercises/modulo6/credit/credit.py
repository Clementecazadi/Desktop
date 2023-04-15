from cs50 import get_int
from math import trunc

def main():
    credit_card = get_int("Número: ")
    card_ok(credit_card)

def card_ok(card):
    #TODO Criar essa função
    next = 1
    current_number = 0
    number_card = card
    type_card = 0
    add = 0
    while True:
        if number_card == 0:
            type_card = current_number
            break
        current_number = number_card % 10
        if next % 2 == 0:
            n = current_number * 2
            if n > 9:
                add += n // 10
                add += n % 10
            else:
                add += n

        number_card = trunc(number_card / 10)
        next += 1

    length_card = next - 1
    next = 1
    number_card = card
    while True:
        if number_card == 0:
            break
        current_number = number_card % 10
        if next % 2 != 0:
            add += current_number
        number_card = trunc(number_card / 10)
        next += 1
    if add % 10 == 0 and  10 < length_card <= 16:
        if type_card == 5:
            print("MASTERCARD")
        elif type_card == 3:
            print("AMEX")
        elif type_card == 4:
            print("VISA")
    else:
        print("INVALID")


main()
