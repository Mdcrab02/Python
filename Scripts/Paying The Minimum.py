balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

totalPaid = 0.0

for i in range(1,13):
    print("Month: " + str(i))
    currentMinPayment = (monthlyPaymentRate*balance)
    currentMinPayment = round(currentMinPayment,2)
    print("Minimum monthly payment: " + str(currentMinPayment))
    balance -= currentMinPayment
    monthlyInterest = annualInterestRate/12.0
    balance = balance + (monthlyInterest*balance)
    balance = round(balance,2)
    print("Remaining Balance: " + str(balance))
    totalPaid += currentMinPayment
    totalPaid = round(totalPaid,2)
print("Total Paid: " + str(totalPaid))
print("Remaining balance: " + str(balance))    