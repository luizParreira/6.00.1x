





def lowest_month_pay(balance, air):
    
    '''
        Math Involved
        mir = air / 12.0
        
        minimum_payment = current_balance * mir
        unpaid_balance = previous_balance - minimum_payment
        update_balance = unpaid_balance + (mir * unpaid_balance)
        
        Should Print:
        Lowest Payment: 310

    '''
    
    
    current_balance = balance
    mir = (air) / 12.0
    m = 0
    payment = 0
   
    while m <= 12:
        
        unpaid_balance = current_balance - payment
        update_balance = unpaid_balance + (mir * unpaid_balance)
        current_balance = update_balance        
        print "m = " + str(m)
        if current_balance <= 0:
            return "Lowest Payment: "+  str(payment)
        if m == 12:
            m = 0
            current_balance = balance
            unpaid_balance = 0
            update_balance = 0
            payment += 0.01
        m += 1
            


balance = 320000
annualInterestRate = 0.2

print lowest_month_pay(balance, annualInterestRate)