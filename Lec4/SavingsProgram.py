# Get information from the user ? Input
balance = float(input('How much do u want to save : '))

if balance <= 0:
    print('Looks like you already have enough')
    balance = 0
    payment = 1
else:
    payment = float(input('How much will you save each period: '))
    if payment <= 0:
        payment = float(input('enter a positive value: '))

# Calculation

num_remaining_payments = balance / payment

# Presentation to the user / Output
print(num_remaining_payments)
print('You must make ' + str(num_remaining_payments) + ' more payments')


