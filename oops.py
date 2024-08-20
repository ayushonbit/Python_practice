class Car:
   def __init__ (self, brand,model): #this init is also known as constructor
      self.brand = brand
      self.model = model


myCar = Car("Toyota","fortuner")
print(myCar.brand)  

def full_Name(self):
   return f"{self.brand} {self.model}"


class ElectricCar(Car): ## ERROR!! maine yha class ki jgh def dedia tha 
   def __init__(self,brand,model,Batterysize): ##brand aur model upar say 
      super().__init__(brand,model) # Super mtlb apne say upar wali class ka access lia aur dono attributes ko call krlia
      self.Batterysize = Batterysize

myElecCar = ElectricCar("Tesla","Model S","XYZ kwh")
print(myElecCar.model)
