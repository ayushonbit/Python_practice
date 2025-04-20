
class balanceException(Exception) :
    pass



class bank_Account :
    def __init__(self,initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\n Account {self.name} created with initial balance ${self.balance:.2f}")

    
    def getBalance(self):
      
         print(f"\n Account {self.name} created with initial balance ${self.balance:.2f}")


    
    
    def deposit(self, amount ):
        self.balance +=amount
        print(f"\n Account {self.name} created with initial balance ${self.balance:.2f}")




    def viableTransaction(self,amount):
        if self.balance>=amount:
            return
        else:
            raise balanceException(f"\n {self.name} only has a balance of {self.balance:.2f}")
        

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print(f"\n withdraw completed")
            self.getBalance()
            
        except balanceException as error:
            print(f"\n withdraw interuptted :{error}")
    

    def tansfer(self,amount, account):
    
        try:
            print(f"\n***********")
            print(f"Initiating transfer")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"transfer complete")
            print(f"\n***********")
            

        except balanceException as error:
            print(f"\n we are facing this error {error}")


        
    
            
    

