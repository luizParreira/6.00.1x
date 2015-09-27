




def lowPayBisectSearch(balance, air):
    
    
    
    '''
        // Monthly Interest rate
        mir = air / 12.0
        
        // Monthly payment lower bound
        lower = balance / 12
        
        // Monthly payment upper bound
        upper = (balance * (1 + mir)**12) / 12 
    '''
    # Monthly interest rate
    mir = air / 12.0
    
    # upper bound
    upper = (balance * ((1.0 + mir)**12.0)) / 12.0
    
    # lower bound
    lower = balance / 12.0  

    # epsilon to be tested against
    epsilon = 0.01
    
    # to be paid
    tbp = (balance * (1 + mir)**12) / 12.0
    
    # Payment to be tested
    payment = (upper + lower) / 2.0

    top = upper
    current_balance = balance
    total_balance = balance
    while abs(current_balance) >= epsilon:
        
        current_balance = balance
        
        #print " lower = " + str(lower) + " upper = " + str(upper) + " p = " + str(payment) 
        current_balance = check_balance(current_balance, payment, mir)

        if current_balance > 0:
            lower = payment
        else:
            upper = payment
        payment = (upper + lower) / 2.0
        total_balance = payment * 12
        # original_balance = current_balance 
    return round(payment, 2)

def check_balance(current, payment, mir):
    result = current
    for m in range(12):
        unpaid = (result - payment)
        result = unpaid + (mir * unpaid)
    return result

    

# test case 1
# balance = 320000
# annualInterestRate = 0.2

# test case 2
# balance = 999999
# annualInterestRate = 0.18
print str(lowPayBisectSearch(balance, annualInterestRate))