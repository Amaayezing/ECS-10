# Maayez Imam 10/2/2017
# Grade need program

gradeWanted = str(input('Enter the grade you want in the class: '))
# user inputs their desired letter grade

percentNeeded = float(input('Enter the percent you need to get that grade: '))
# user inputs the percent they need to get that letter grade

currentPercent = float(input('Enter your current percent in the class: '))
# user inputs the current grade they have in the class

finalWeight = float(input('Enter the weight of the final: '))
# user inputs the weight of the final

gradeNeeded = float(((percentNeeded * 0.01) - (currentPercent * 0.01 * (1 - (finalWeight * 0.01)))) / (finalWeight * 0.01))
gradeNeeded = gradeNeeded * 100;
# calculates the grade needed on the final, given the desired grade, the current grade, and the weight of the final

print("You need to get at least %.2f%% on the final to get a %c in the class." % (gradeNeeded, gradeWanted))
# prints out the grade the user needs to get the desired grade