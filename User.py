class Create_Account:
    def __init__(self,name,email,password) -> None:
        self.name=name
        self.email=email
        self.password=password

class User(Create_Account):
    def __init__(self,name, email, password, amount) -> None:
        super().__init__(name,email, password)
        self.balance=amount
        self.loan=0
        self.min_withdraw=499
        self.transactions={}
        self.users=[]

    # def add_user(self):
    #     user={'name':self.name,'balance':self.balance}
    #     self.users.append(user)

    def deposit(self,amount):
        if amount>0:
            self.balance += amount

    def send_money(self,user,amount):
        user.balance += amount
        self.balance -= amount

    def withdrawal(self,amount):
        if amount> self.balance:
            print(f'the bank is bankrupt')
        elif amount < self.min_withdraw:
            print(f'Can not withdraw less than {self.min_withdraw}')
        else:
            self.balance -= amount

    def take_loan(self,amount):
        total_loan=0
        if((self.balance * 2) >= amount):
            self.balance += amount
            total_loan += amount
            self.loan = total_loan

    def get_balance(self):
        return f'Hi {self.name} Your balance: {self.balance}'
    
    def transfer_money(self,amount):
        if amount<self.balance:
            self.balance -= amount

    def transaction_history(self):
        pass


# user1=User('aka','u@u.com','1212',1000)
# user1.add_user()
# user1.deposit(1200)
# user1.withdrawal(50)
# print(user1.get_balance())

# user2=User('baka','u@u.com','1212',100)
# user2.add_user()
# user2.deposit(1200)
# user2.withdrawal(500)
# print(user2.get_balance())