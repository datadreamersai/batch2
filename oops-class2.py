class AtmBasicFunctionalities():
    def __init__(self,balance_amount):#constructor, also it is one of the special/dunder method
        
        self.balance = balance_amount

    def check_balance(self):
        return "Your current balance is {}".format(self.balance)
    

    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount#self.balance=self.balance-amount
            return "please collect your withdraw amount : {}".format(amount)
        else:
            return "Insufficient Balance"
        
    
    def deposit(self,amount):
        self.balance+=amount#self.balance=self.balance+amount
        return "Your updated balance is : {}".format(self.balance)
    


sbi = AtmBasicFunctionalities(1000)#instation of an object
print(sbi.check_balance())
print(sbi.deposit(1000))
print(sbi.withdraw(500))
print(sbi.check_balance())


    







class LoanFunctionalities():
    
    def __init__(self,interest,foreclose_tenure_in_years,min_loan_amount,min_tenure_in_years):
        self.roi=interest
        self.foreclosure_tenure = foreclose_tenure_in_years
        self.min_loan_amount = min_loan_amount
        self.min_tenure_in_years = min_tenure_in_years


    def loan_credibility_check(self,employed):
        if employed:
            return "Great, You are eligible for loan amount"
        else:
            return "Please get job first to get loan"
        
    def interest_cal(self,amount,tenure_in_years):
        if (amount>=self.min_loan_amount) and (tenure_in_years>=self.min_tenure_in_years):
            s_i = (amount*tenure_in_years*self.roi)/100
            return "you will pay extra {} for the loan amount {}".format(s_i,amount)
        
        else:
            return "Invalid input, please enter loan amount >=50000 and tenure in years >=1"
        
    def foreclosure(self,tenure_paid_in_years):
        if tenure_paid_in_years>self.foreclosure_tenure:
            return "Great, You are eligible for foreclosure"
        else:
            return "Sorry, Not eligible for foreclosure"


print("SBI related")
sbi_loan = LoanFunctionalities(0.1,3,50000,1)
print(sbi_loan.loan_credibility_check(True))
print(sbi_loan.interest_cal(500000,5))
print(sbi_loan.foreclosure(2))



print("HDFC related")
hdfc_loan= LoanFunctionalities(0.2,1,100000,2)
print(hdfc_loan.loan_credibility_check(True))
print(hdfc_loan.interest_cal(500000,5))
print(hdfc_loan.foreclosure(2))



