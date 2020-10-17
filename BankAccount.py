class BankAccount:
    
    def __init__(self, accNumber, name, balance):  #init constructor to initialise params
        self.accNumber = accNumber   
        self.name = name
        self.balance = balance
    
    def deposit(self, income, balance):   
        income = input("Money to deposit: ")          #stores the user income to deposit
        if len(income) != 0:                          #if something is entered
            self.balance = (int(balance) + int(income))        #add the user entry to the balance as the object balance 
        else:
            print("No deposit required")
        
    def withdrawal(self, outcome, balance):
        outcome = input("Money to take out: ")        #stores the user withdrawal amount
        if outcome:
            self.balance = (int(balance) - int(outcome))    #takes the withdrawal amount from the balance as the object balance
        else:
            print("No withdrawal required")
        
        
        
    def display(self):                        #display method to show all the data entries
        print("Account: ", self.accNumber)             
        print("Name: ", self.name)
        print("Balance: ", self.balance)
        
conor = BankAccount(1223,"conor",12300)
conor.deposit(1200, conor.balance)
conor.withdrawal(1000, conor.balance)
conor.display()
