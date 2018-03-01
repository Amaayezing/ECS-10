#Maayez Imam 10/30/17
#Fraction Add Program


def fraction_add():
    fraction_one = (input("Enter a fraction: "))
    while fraction_one.isalpha():
        fraction_one = (input("Enter a fraction: "))
    while not fraction_one.strip()[0] == '-' and not fraction_one.strip()[1:].isdigit():
        fraction_one = (input("Enter a fraction: "))
    if '/' in fraction_one:
        numerator_one = int(fraction_one.split('/')[0])
        denominator_one = int(fraction_one.split('/')[1])
    else:
        fraction_one = fraction_one + '/1'
        numerator_one = int(fraction_one.split('/')[0])
        denominator_one = int(fraction_one.split('/')[1])

    fraction_two = (input("Enter another fraction: "))
    while fraction_two.isalpha():
        fraction_two = (input("Enter another fraction: "))
    if '/' in fraction_two:
        numerator_two = int(fraction_two.split('/')[0])
        denominator_two = int(fraction_two.split('/')[1])
    else:
        fraction_two = fraction_two + '/1'
        numerator_two = int(fraction_two.split('/')[0])
        denominator_two = int(fraction_two.split('/')[1])

    # if denominator_one != denominator_two:
    new_denominator_one = denominator_one * denominator_two
    new_numerator_two = numerator_two * denominator_one
    new_numerator_one = numerator_one * denominator_two
    new_denominator_two = new_denominator_one

    final_numerator = new_numerator_one + new_numerator_two
    final_denominator = new_denominator_one

    if final_numerator % 25 == 0 and final_denominator % 25 == 0:
        final_numerator = final_numerator / 25
        final_denominator = final_denominator / 25

    if final_numerator % 10 == 0 and final_denominator % 10 == 0:
        final_numerator = final_numerator / 10
        final_denominator = final_denominator / 10

    if final_numerator % 9 == 0 and final_denominator % 9 == 0:
        final_numerator = final_numerator / 9
        final_denominator = final_denominator / 9

    if final_numerator % 8 == 0 and final_denominator % 8 == 0:
        final_numerator = final_numerator / 8
        final_denominator = final_denominator / 8

    if final_numerator % 7 == 0 and final_denominator % 7 == 0:
        final_numerator = final_numerator / 7
        final_denominator = final_denominator / 7

    if final_numerator % 6 == 0 and final_denominator % 6 == 0:
        final_numerator = final_numerator / 6
        final_denominator = final_denominator / 6

    if final_numerator % 5 == 0 and final_denominator % 5 == 0:
        final_numerator = final_numerator / 5
        final_denominator = final_denominator / 5

    if final_numerator % 4 == 0 and final_denominator % 4 == 0:
        final_numerator = final_numerator / 4
        final_denominator = final_denominator / 4

    if final_numerator % 3 == 0 and final_denominator % 3 == 0:
        final_numerator = final_numerator / 3
        final_denominator = final_denominator / 3

    if final_numerator % 2 == 0 and final_denominator % 2 == 0:
        final_numerator = final_numerator / 2
        final_denominator = final_denominator / 2

    (print("%s/%s + %s/%s = %d/%d" % (numerator_one, denominator_one, numerator_two, denominator_two, final_numerator,
                                      final_denominator)))


fraction_add()
