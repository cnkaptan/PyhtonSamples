# balance = 42
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04
#
# for i in range(0, 12):
#     minPayment = balance * monthlyPaymentRate
#     balance = balance - minPayment
#     interest = balance * (annualInterestRate / 12)
#     balance += interest
#
# balance = round(balance, 2)
# print('Remaining balance: ', balance)
#
#
# annualInterestRate = 0.2
# monthlyInterestRate = annualInterestRate / 12.0
# print(monthlyInterestRate)
# for i in range(0,12):
#     monthlyUnpaidBalance = balance - 304
#     balance = monthlyUnpaidBalance + (monthlyUnpaidBalance*monthlyInterestRate)
print('--------------------------')
# increase = 0.01
# middle = 0
# fixbalance = 3926
# monthlyInterestRate = 0.2 /12.0
# balance = fixbalance
# while True:
#     for i in range(0, 12):
#         monthlyUnpaidBalance = balance - startPayment
#         balance = monthlyUnpaidBalance + (monthlyUnpaidBalance * monthlyInterestRate)
#     if balance <= 0:
#         print('Lowest Payment:',startPayment)
#         break
#     else:
#         print(balance,startPayment)
#         balance = fixbalance
#         startPayment += increase
print('--------------------------')
balance = 320000
annualInterestRate = 0.2
tryBalance = balance
monthlyInterestRate = annualInterestRate / 12.0
lowerBound = balance / 12
upperBound = (balance * ((1 + monthlyInterestRate) ** 12)) / 12
middle = (lowerBound + upperBound) / 2
while True:
    for i in range(0, 12):
        monthlyUnpaidBalance = tryBalance - middle
        tryBalance = monthlyUnpaidBalance + (monthlyUnpaidBalance * monthlyInterestRate)
    if tryBalance < 0:
        upperBound = middle
    else:
        lowerBound = middle
    if round((lowerBound + upperBound) / 2, 2) == round(middle, 2):
        print('Lowest Payment:', round(middle,2))
        break
    else:
        middle = (lowerBound + upperBound) / 2
        tryBalance = balance
