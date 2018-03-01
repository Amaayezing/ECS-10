#Maayez Imam 10/21/17
#Pi Program

import random
import math

def random_coordinate():
    return random.uniform(-1, 1)


seed = int(input("Enter the seed for the random number generator: "))
random.seed(seed)
points_picked = int(input("Enter the number of iterations to run: "))
points_circle = int()
i = int(0)
x_axis = float()
y_axis = float()
pi = float()
prob_circle = float()

for i in range(points_picked):
    x_axis = random_coordinate()
    y_axis = random_coordinate()

    if ((x_axis ** 2) + (y_axis ** 2)) <= 1:
        points_circle = points_circle + 1

prob_circle = float(points_circle) / float(points_picked)
pi = prob_circle * 4

print("The value of pi is %.3f." % pi)


