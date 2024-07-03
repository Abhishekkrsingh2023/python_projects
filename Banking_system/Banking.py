'''
    This is a Program to create and manage the account and holdings 
    of a Bank customer usnig the class and objects fundamentals
'''

class Bank:
    cust_cnt = 0 # class attribute to manage the customer count
    __cust_details = list()
    __pin = "1234"
    # The constructor method
    def __init__(self, name, age, balance, acc_no):
        self.name = name
        self.age = age
        self.__balance = balance # creating a private attribute balance for each instance
        Bank.cust_cnt = Bank.cust_cnt + 1 # incrementing customer count after each instance creating
        self.acc_no = acc_no
        # storing individual instances into the list
        Bank.__cust_details.append(self)

    # getter to get the balance
    def get_balance(self):
        pin=int(input("Enter Pin : "))
        if(pin == self.__pin):
            return self.__balance
        else:
            print("Invalid pin")
    
    # Abstracted method
    def __debit_balnace(self):
        pin=int(input("Enter Pin : "))
        if(pin == self.__pin):
            amt = int(input("Enter the amout to Debit : "))
            if self.__balance > amt:
                self.__balance = self.__balance - amt
                print(f"Tranxation of {amt} is successful")
            else:
                print("Insuffient Balance")
        else:
            print("Invalid Pin ")
    
    # Abstracted method
    def __credit_balance(self):
        pin=int(input("Enter Pin : "))
        if(pin == self.__pin):
            amt = int(input("Enter the amount to Credit : "))
            if amt >=0:
                self.__balance = self.__balance + amt
                print(f"Credited {amt} successfully")
            else:
                print("Invalid amount")
        else:
            print("Invalid pin")
        
    # function to generate New_pin
    def __pin_Gen(self):
        pin = int(input("Enter New 4 digit Pin : "))
        self.__pin = pin
        print("Pin set successful")
    
    # to perform atm operations
    @classmethod 
    def atm_op(cls):
        # for find the customer
        account_no = int(input("Enter your account number : "))
        check = False
        for i in Bank.__cust_details:
            if(account_no == i.acc_no):
                while(True):
                    check = True
                    print(''' Enter the transaction to perform :

                          press 1 for pin genreate 
                          press 2 for withdraw
                          press 3 for Credit
                          press 4 for Banlance enquiry
                          press 5 for exit

                          ''' )
                    choice = int(input("Enter choice : "))
                    if(choice == 1):
                        i.__pin_Gen()
                    elif(choice == 2):
                        i.__debit_balnace()
                    elif(choice == 3):
                        i.__credit_balance()
                    elif(choice == 4):
                        print("Balance : ",i.__balance)
                    else:
                        print(f"Thank You {i.name} for the trasaction")
                        print("Exit")
                        break
        if(check == False):
            print("Customer Not found")

# All the account holders   
cust1 = Bank("Abhishek",20,65000, 1234)
cust2 = Bank("Suman",19,98000, 2255)
cust3 = Bank("Suvadwip",19,80000, 9785)
cust4 = Bank("Soumajit", 19, 365000, 3364)
cust5 = Bank("Souvick", 19, 67000,9999)
cust6 = Bank("Arnab", 19, 99000, 7456)
cust6 = Bank("Akash", 19, 123000, 5064)
cust6 = Bank("Sumit", 20, 90000, 11123)
cust6 = Bank("Arvind", 20, 55000, 34568)

Bank.atm_op()