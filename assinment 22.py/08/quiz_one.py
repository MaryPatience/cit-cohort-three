#1.Using classes, Create a basic banking application with the following features:
    #Create a class called BankAccount with the following attributes:
        #account_number - a string
        #balance - a float
        #owner - a string
        #type - a string
class BankAccount:
    def __init__(self,account_number, balance, owner, type ):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.type = type

    #ii.Create a class called Bank with the following attributes:
        #name - a string
        #accounts - a list of BankAccount objects
class Bank:
    def __init__(self,name,accounts):
        self.name = name
        self.accounts = accounts

    #iii.Create a class called Customer with the following attributes:
        #name - a string
        #accounts - a list of BankAccount objects
class Customer:
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts

    #iv.Create a class called Transactions with the following attributes:
        #1. `account` - a `BankAccount` object
        #2. `amount` - a float
        #3. `type` - a string
class Transactions:
    def __init__(self, account, amount, type,):
        self.account = account
        self.amount  = amount
        self. type = type
  

#The application should have the following functionality:
    #Create a new Bank object
    #Create a new Customer object
    #Create a new BankAccount object
    #Add the BankAccount object to the Bank object
    #Add the BankAccount object to the Customer object
    #Print the Bank object
    #Print the Customer object
    #Print the BankAccount object
    #Create a new Transaction object
    #Add the Transaction object to the BankAccount object

print("         ABSA BANK           ")
print("         Welcome!!           ")

Acc1 = BankAccount('0123456789', 120000.00,'Kizzah Lawrence', 'Savings Account')  #BankAccount object

lst = [[Acc1.account_number, Acc1.balance, Acc1.owner, Acc1.type],[]] #list of bank account objects

Bank1 =Bank('Kizzah Lawrence', lst[0]) #Bank object

Cus = Customer('Kizzah Lawrence', lst[0])

print (f'''
           BankAccount object
           Account Number : {Acc1.account_number}
           Account Balance: {Acc1.balance}
           Account Name   : {Acc1.owner}
           Account Type   : {Acc1.type} ''') #Print the BankAccount object

print(f''' 
           Bank object
           Account Number : {Bank1.accounts[0]}
           Account Balance: {Bank1.accounts[1]}
           Account Name   : {Bank1.name}
           Account Type   : {Bank1.accounts[3]} ''') #Print the Bank object

print(f''' 
           Customer object
           Account Number : {Cus.accounts[0]}
           Account Balance: {Cus.accounts[1]}
           Account Name   : {Cus.name}
           Account Type   : {Cus.accounts[3]} ''') #Print the Customer object

trans = Transactions(lst[0], 100000.00, 'Deposit') #Create a new Transaction object


