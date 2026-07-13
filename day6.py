#Encapsulation is wrapping up of variables and methods 
#together inside a class and controlling access of the data 

class bank:
    def __init__(self):
        self.balance=1000
account=bank()
account.balance=10000000
print(account.balance)


class bank:
    def __init__(self):
        self._balance=1000
    def deposit(self,amount):
        self._balance+=amount
    def show_balance(self):
        print(self._balance)
account=bank()
account.deposit(5000)
account.show_balance()

# getter

class employee:
    def __init__(self,salary):
        self._salary=salary
    def get_salary(self):
        return self._salary
emp=employee(52836)
print(emp.get_salary())


# setter method

class employee:
    def __init__(self):
        self._salary=0
    def set_salary(self,amount):
        if amount>0:
            self._salary=amount
        else:
            print("Invalid Salary")
    def get_salary(self):
        return self._salary

emp=employee()
emp.set_salary(52836)
print(emp.get_salary())

# Polymorphism


class dog:
    def sound(self):
        print("Dog barks")
class cat:
    def sound(self):
        print("Cat meows")
class sparrow:
    def sound(self):
        print("Sparrow chirps")       
Dog=dog()
Cat=cat()
Sparrow=sparrow()
Dog.sound()
Cat.sound()
Sparrow.sound()


# Abstraction

# Abstraction means hiding internal implementation and
# Showing only necessary features to the user

from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class car(vehicle):
    def start(self):
        print("Car started")
car=car()
car.start()

from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class dog(animal):
    def sound(self):
        print("Dog barks")
class donkey(dog):
    def sound(self):
        print("Donkey kicked")
donkey=donkey()
donkey.sound()










































