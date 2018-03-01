#Maayez Imam 10/2/2017
#Change program

moneyWithdrawn = int(input('Please enter the amount of money you wish to withdraw: '))
ones = 0
fives = 0
tens = 0
twenties = 0
fifties = 0
hundreds = 0
modhundreds = 0
modfifties = 0
modtwenties = 0
modtens = 0
modfives = 0

hundreds = moneyWithdrawn / 100
modhundreds = moneyWithdrawn % 100

fifties = modhundreds / 50
modfifties = modhundreds % 50

twenties = modfifties / 20
modtwenties = modfifties % 20

tens = modtwenties / 10
modtens = modtwenties % 10

fives = modtens / 5
modfives = modtens % 5

ones = modfives % 5

print("You received %d hundred(s)" %hundreds)
print("You received %d fifty(s)" %fifties)
print("You received %d twenty(s)" %twenties)
print("You received %d ten(s)" %tens)
print("You received %d five(s)" %fives)
print("You received %d one(s)" %ones)



