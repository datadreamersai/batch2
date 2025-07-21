
balance=1000

def deposit(deposit_amount):
    global balance
    if deposit_amount>0:
        balance=balance+deposit_amount
        return "Your updated balance is {}".format(balance)
    else:
        return "Please enter valid amount"
    


def withdraw(withdraw_amount):
    global balance
    if withdraw_amount<=balance:
        balance=balance-withdraw_amount*2
        return "Your balance left is {}".format(balance)
    else:
        return "Insufficent Balance"
    

def check_balance():
    return "your existing balance is {}".format(balance)



def credit_score():
    pass

def loan_eligibility_check():
    pass

def credit_card_balance():
    pass

def car_loan_eligibility():
    pass

def credit_Card_summary(months):
    pass



deposit_amount = int(input("Please enter deposit amount:"))

withdraw_amount = int(input("Please enter withdraw amount:"))

out= deposit(deposit_amount)
print(out)

out = withdraw(withdraw_amount)
print(out)

out = check_balance()
print(out)