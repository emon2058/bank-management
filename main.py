from User import User
from Admin import Admin
def main():
    admin=Admin('admim','admin@g.com','1111')
    user1=User('aka','u@u','121212',12000)
    user1.deposit(1000)
    user1.withdrawal(500)
    user1.take_loan(1500)
    print(user1.get_balance())
    admin.loan_feature('off')
    user2=User('bkash','uqq@u','121212',12000)
    user2.deposit(2000)
    user2.send_money(user1,2000)
    user2.withdrawal(60000)
    print(user2.get_balance())
    print(user1.get_balance())
    user2.take_loan(1000)
    print(user2.get_balance())
    
    print(admin.check_balance(user1,user2))
    print(admin.total_loan([user1,user2]))

    
if __name__=='__main__':
    main()