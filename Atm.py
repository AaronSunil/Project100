class atm:
    def __init__(self,atmcardNumber,pinNumber):
        self.atmcardNumber = atmcardNumber
        self.pinNumber = pinNumber
    def CashWithdrawl(self):
        print("For Cash Withdrawal, please input the amount to be withdrawn: ")
    def BalanceEnquiry(self):
        print("For Balance Enquiry, please check if the atmcard number is correct: " + self.atmcardNumber)
        print("For Balance Enquiry, please check if the pin number is correct: " + self.pinNumber)
    def Deposit(self):
        print("For Depositing, please visit a bank")


