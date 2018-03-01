#Maayez Imam 10/1/2017
#Loan cost program

Borrowed = input('Please enter the amount of money you borrowed: $') #asks user for how much they initially borrowed
Borrowed = float(Borrowed)
round(Borrowed, 2)
AnnualInterestRate = input('Please enter the annual interest rate: ') #asks user for what their annual interest rate is
AnnualInterestRate = float(AnnualInterestRate)
round(AnnualInterestRate, 2)
Payments = input('Please enter the number of payments to be made: ') #asks user for the number of payments they will be making
Payments = int(Payments)
round(Payments, 2)

MonthlyInterestRate = AnnualInterestRate / 12 #calculates the monthly interest rate by dividing the annual interest rate by 12
round(MonthlyInterestRate, 2)
MonthlyPayment = ((MonthlyInterestRate * Borrowed) / (1 - (1 + MonthlyInterestRate)**(-Payments))) #calculates the monthly payment by using the given formula and the new monthly interest rate value
round(MonthlyPayment, 2)
LoanCost = Payments * MonthlyPayment #calculates the loan cost by multiplying the number of payments by the monthly payments
round(LoanCost, 2)
FinalLoanCost = LoanCost - Borrowed #calculates the final loan coast by subtracting the amount borrowed by the loan coast
round(FinalLoanCost, 2)

print('A loan of $%.2f with an annual interest of %.2f payed off over %d months will have monthly payments of $%.2f.' % (Borrowed, AnnualInterestRate, Payments, MonthlyPayment))
print("In total you will pay $%.2f, making the cost of your loan $%.2f." % (LoanCost, FinalLoanCost))