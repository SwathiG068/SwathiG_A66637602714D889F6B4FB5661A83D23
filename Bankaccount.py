class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance = 0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
    
  def deposit (self, amount):
    if amount > 0:
      self.__account_balance += amount
      # self.__account_balance = self.__account_balance+amount 
      print("\nDeposited Amount :  ₹{}. \nNew balance : ₹{}".format(amount,self.__account_balance))
      
    else:
      print("\nInvalid deposit amount.")

  def withdraw(self, amount):          
    if amount > 0 and amount<= self.__account_balance:
      self.__account_balance -= amount
      # self.__account_balance = self.__account_balance - account
      print("\nWithdraw Amount :₹{}. \nNew balance: ₹{}".format(amount,
self.__account_balance)) 
    else: 
      print("\nInvalid withdrawal amount or Insufficient Balance.")

  def display_balance(self):           
    print("Account balance for {} \n(Account Number is {}):     ₹ {}".format(
self.__account_holder_name,
self.__account_number,
self.__account_balance))
    
# Create an instance of the BankAccount class
account = BankAccount(account_number= "222204068",
              account_holder_name="Swathi",
                      initial_balance= 5000.00)

# Test deposit and withdrawal functionality
account.display_balance()
account.deposit(500.00)
account.withdraw(200.00)
account.withdraw(20.00)
account.withdraw(10000.00)

account.display_balance()