from User import Create_Account
class Admin(Create_Account):
    def __init__(self, name,email, password) -> None:
        super().__init__(name,email, password)
        self.balance=10000000
        self.loan=True
        self.loan_amount=None

    def check_balance(self,*users):
        total=0
        for user in users:
            total += user.balance
        self.balance += total
        return self.balance

    def total_loan(self,users):
        total=0
        for user in users:
            total += user.loan
        return total

    def loan_feature(self,feature):
        if self.balance<100000 or feature == 'off' :
            self.loan=False
        else:
            self.loan=True


