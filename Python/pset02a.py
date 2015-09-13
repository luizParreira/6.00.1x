


def calculate_pay(b, air, mpr):
    
    '''
        Print to the console
        "
        b = balance
        air = annualInterestRate
        mpr  monthlyPaymentRate
        
        Month: 1
        Minimum monthly payment: 96.0
        Remaining balance: 4784.0
        
        unpaid_balance = balance - payment_made
        
        next balance = unpaid_balance + (air/12.0) * unpaid_balance
        
        mmp = curent_balance * 0.02
    '''
    
    current_balance = 0.0
    payment = 0.0
    previous_balance = b
    total_paid = 0 
    for i in range(12):
        payment = previous_balance * mpr
        unpaid_balance = previous_balance - payment
        current_balance = unpaid_balance + ((air/12.0) * unpaid_balance)
        
        print 'Month: ' + str(i +1)
        print 'Minmum monthly Payment: ' + str(round(payment, 2))
        print 'Remaining balance: ' + str(round(current_balance, 2))
        total_paid += payment
        previous_balance = current_balance
    print 'Total paid: ' + str(round(total_paid, 2))
    print 'Remaining balance: ' + str(round(current_balance, 2))

    
balance = 3329
annualInterestRate = 0.2
calculate_pay(balance, annualInterestRate, annualInterestRate / 12.0)
print "\n*********\n"
#calculate_pay(4842 , 0.2, 0.04)

        