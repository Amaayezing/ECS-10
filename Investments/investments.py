#Maayez Imam 10/18/17
#Investments Program

import random
import math

def investments():
    loan_amount = float(input("Enter how much money you owe in loans: "))
    while loan_amount < 0:
        loan_amount = float(input("Enter how much money you owe in loans: "))

    interest_rate_loan = float(input("Enter the annual interest rate of the loans: "))
    while interest_rate_loan < 0:
        interest_rate_loan = float(input("Enter the annual interest rate of the loans: "))

    loan_payment_minimum = float(input("Enter your minimum monthly loan payment: "))
    while loan_payment_minimum < 0:
        loan_payment_minimum = float(input("Enter your minimum monthly loan payment: "))

    payment_monthly = float(input("Enter how much money you will be putting towards loans/retirement each month: "))
    while payment_monthly < 0 or payment_monthly <= loan_payment_minimum:
        payment_monthly = float(input("Enter how much money you will be putting towards loans/retirement each month: "))

    age_current = int(input("Enter your current age: "))
    while age_current < 0:
        age_current = int(input("Enter your current age: "))

    age_retirement = int(input("Enter the age you plan to retire at: "))
    while age_retirement < 0 or age_retirement < age_current:
        age_retirement = int(input("Enter the age you plan to retire at: "))

    interest_rate_investment = float(input("Enter your predicted annual rate of return: "))
    while interest_rate_investment < 0:
        interest_rate_investment = float(input("Enter your predicted annual rate of return: "))

    payment_total_max = float()
    payment_total_min = float()
    months_payment = int()

    #payment_monthly = getValidMonthlyPayment()

    #loan_amount = getValidLoanAmount()

    #interest_rate_loan = getValidLoanInterestRate()

    #loan_payment_minimum = getValidMinimumLoanPayment()

    #if payment_monthly < loan_payment_minimum:
     #   print("You didn't set aside enough money to pay off our loans. Ending program.\n")
      #  exit(0)

    #age_current = getValidCurrentAge()

    #age_retirement = getValidRetirementAge(age_current)

    #interest_rate_investment = getValidInvestmentInterestRate()

    months_payment = (age_retirement - age_current) * 12

    payment_total_max = max_monthly_payment(loan_amount, payment_monthly, interest_rate_loan, interest_rate_investment, months_payment)
    payment_total_min = min_monthly_payments(loan_amount, loan_payment_minimum, payment_monthly, interest_rate_loan, interest_rate_investment, months_payment)

    if payment_total_min > payment_total_max:
        print("You should only make minimum payments on your loans and invest the rest\n"
              "If you do you will have $%.2f as opposed to $%.2f when you retire.\n" % (payment_total_min, payment_total_max))

    if payment_total_max > payment_total_min:
        print("You should pay of all of your loans before you start investing\n"
              "If you do you will have $%.2f as opposed to $%.2f when you retire.\n" % (payment_total_max, payment_total_min))


# def getValidMonthlyPayment():
#     monthlyPayment = float()
#     numArgsRead = int()
#
#     while (not(isValidFormatting(numArgsRead, 1))) or (not(monthlyPayment >= 0)):
#         print("Enter how much money you will be putting towards loans/retirement each month: ")
#         numArgsRead = input(" %f" % monthlyPayment)
#
#     return monthlyPayment


# def getValidLoanAmount():
#
#     loanAmount = float()
#     numArgsRead = int()
#
#     while (not(isValidFormatting(numArgsRead, 1)) or (not(loanAmount >= 0))):
#         print("Enter how much you owe in loans: ")
#         numArgsRead = input(" %lf" % loanAmount)
#
#     return loanAmount


# def getValidLoanInterestRate():
#
#     loanInterestRate = float()
#     numArgsRead = int()
#
#     while (not(isValidFormatting(numArgsRead, 1)) or (not(loanInterestRate >= 0))):
#         print("Enter the annual interest rate of the loans: ")
#         numArgsRead = input(" %lf" % loanInterestRate)
#
#     return loanInterestRate


# def getValidMinimumLoanPayment():
#
#     minimumLoanPayment = float()
#     numArgsRead = int()
#
#     while (not(isValidFormatting(numArgsRead, 1)) or (not(minimumLoanPayment >= 0))):
#         print("Enter your minimum monthly loan payment: ")
#         numArgsRead = input(" %lf" % minimumLoanPayment)
#
#     return minimumLoanPayment


# def getValidCurrentAge():
#
#     currentAge = int()
#     numArgsRead = int()
#
#     while (not(isValidFormatting(numArgsRead, 1)) or (not(currentAge >= 0))):
#         print("Enter your current age: ")
#         numArgsRead = input(" %d" % currentAge)
#
#     return currentAge


# def getValidRetirementAge(currentAge):
#
#     retirementAge = int()
#     numArgsRead = int()
#
#     while (not(isValidFormatting(numArgsRead, 1)) or (not(retirementAge >= 0)) or (retirementAge < currentAge)):
#         print("Enter the age you plan to retire at: ")
#         numArgsRead = input(" %d" % retirementAge)
#
#     return retirementAge

# def getValidInvestmentInterestRate():
#
#     investmentInterestRate = float()
#     numArgsRead = int()
#
#     while (not(isValidFormatting(numArgsRead, 1)) or (not(investmentInterestRate >= 0))):
#         print("Enter the annual rate of return you predict for your investments: ")
#         numArgsRead = input(" %lf" % investmentInterestRate)
#
#     return investmentInterestRate


def max_monthly_payment(loan_amount, payment_monthly, interest_rate_loan, interest_rate_investment, months_payment):

    savings = float(0.00)
    excess = float(0.00)
    i = int()

    for i in range(months_payment):
        if loan_amount == 0.00:
            savings = savings + (savings * (interest_rate_investment / 12))
            savings = savings + payment_monthly

        elif loan_amount < payment_monthly:
            loan_amount = loan_amount + (loan_amount * (interest_rate_loan / 12))
            excess = payment_monthly - loan_amount
            savings = savings + excess
            loan_amount = 0.00

        elif loan_amount >= payment_monthly:
            loan_amount = loan_amount + (loan_amount * (interest_rate_loan / 12))
            loan_amount = loan_amount - payment_monthly

    return savings


def min_monthly_payments(loan_amount, loan_payment_min, payment_monthly, interest_rate_loan, interest_rate_investment, months_payment):

    savings = float(0.00)
    excess = float(0.00)
    i = int()

    for i in range(months_payment):

        if loan_amount == 0.00:
            savings = savings + (savings * (interest_rate_investment / 12))
            savings = savings + payment_monthly

        elif loan_amount < loan_payment_min:
            loan_amount = loan_amount + (loan_amount * (interest_rate_loan / 12))
            excess = payment_monthly - loan_amount

            savings = savings + (savings * (interest_rate_investment / 12))
            savings = savings + excess
            loan_amount = 0.00

        elif loan_amount >= loan_payment_min:
            loan_amount = loan_amount + (loan_amount * (interest_rate_loan / 12))
            loan_amount = loan_amount - loan_payment_min

            savings = savings + (savings * (interest_rate_investment / 12))
            savings = savings + (payment_monthly - loan_payment_min)

    if loan_amount > 0.00:
            print("Warning after you retire you will still have $%.2f in loans left.\n" % loan_amount)

    return savings


# def isValidFormatting(numArgsRead, numArgsNeeded):
#
#     newLine = '\n'
#     isValid = True
#
#     if numArgsRead != numArgsNeeded:
#         isValid = False
#         input("%c" % newLine)
#     if not newLine.isspace():
#         isValid = False
#
#     while newLine != '\n':
#
#         return isValid


investments()