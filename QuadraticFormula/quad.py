#Maayez Imam 10/9/2017
#Loan cost program

import math

print('Given a quadratic equation of the form a*x^2 + b * x + c\n')
a = float(input('Please enter a: '))
b = float(input('Please enter b: '))
c = float(input('Please enter c: '))


def quadratic_formula(num_a, num_b, num_c):
    realsolution1 = 0
    realsolution2 = 0
    if (num_a != 0) and (num_b > (math.sqrt(4 * num_a * num_c))):
        realsolution1 = ((-1 * num_b) + (math.sqrt((num_b ** 2)) - (4 * num_a * num_c))) / (2 * num_a)
        realsolution2 = ((-1 * num_b) - (math.sqrt((num_b ** 2)) - (4 * num_a * num_c))) / (2 * num_a)
        print('There are 2 real solutions\n')
        print('Solution 1: %.2lf' % realsolution1)
        print('Solution 2: %.2lf' % realsolution2)

    elif num_b == (math.sqrt(4 * num_a * num_c)):
        realsolution1 = ((-1 * num_b) / (2 * num_a))
        print('There is one real solution: %.2lf' % realsolution1)

    else:
        print('There are no real solutions')


quadratic_formula(a, b, c)