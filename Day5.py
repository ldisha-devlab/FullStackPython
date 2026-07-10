                    #Class and Objects
#  Example 1 

class student:
        name="John Doe"   #class_name
        def study(self):     #represent current object
            print("John Doe is studying.")
s1=student()  #s1 is a object
print(s1.name)
s1.study() #study is method


# Example 2
class student:
    def details(self):
            print("had breakfast")
            
s1=student()
s1.details()    
student.details(s1)


# Constructor 

class student:
    def __init__(self, name,age):
        self.name = name
        self.age= age     
s1 = student("John",20)
s2=student("Smitha",22)
s3=student("Jhanvi",21)
print("S1 Name:",s1.name,",","S1 Age:",s1.age)
print("S2 Name:",s2.name,",","S2 Age:",s2.age)
print("S3 Name:",s3.name,",","S3 Age:",s3.age)


# Method 

class bank:
    def __init__(self, balance):
        self.balance=balance

    def check_balance(self):
        print(self.balance)
account=bank(5000)
account.check_balance()

class user:
    def __init__(self,name):
        self.name=name
    def login(self):
        print(self.name, "has logged in")
u1=user("Bhavitha")
u2=user("John")
u1.login()
u2.login()


# Inheritance


# Single level Inheritance

class father:
    def house(self):
        print("Father has a house.")
class son(father):
    def bike(self):
        print("Son has a bike.")
s1=son()
s1.house()
s1.bike()

# Multi level Inheritance

class grandfather:

    def land(self):
        print("Grandfather has an house.")
class father(grandfather):
    def house(self):
        print("Father has a house.")
class son(father):
    def bike(self):
        print("Son has a bike.")
s1=son()
s1.land()
s1.house()
s1.bike()

# Multiple level

class dad:
    def land(self):
        print("Dad has a land property")
class mom:
    def house(self):
        print("Mom has a house")

class son(dad,mom):
    def gift(self):
        print("Son inherited both land and house")
s1=son()
s1.land()
s1.house()
s1.gift()

# Hierarchial level

class dad:
    def land(self):
        print("Dad has a land property")
class son(dad):
    def house(self):
        print("Son has a house.")
class daughter(dad):
    def gift(self):
        print("Daughter has jewelry gift")
s1=son()
s2=daughter()
s1.land()
s1.house()
s2.land()
s2.gift()

# Magic Methods

class student:
    def __init__(self,name):
        self.name=name
    
    def __str__(self):
        return self.name
s=student("King")
print(s)


#Decorators 

def login(func):
    def  wrapper():
        print("Checking Login")
        func()
    return wrapper
#login
def dashboard():
    print("Dashboard page")
dashboard()


def login(func):
    def  wrapper():
        print("Function ended")
        func()
        print("Function ended")
    return wrapper
#message
def hello():
    print("Hello Python")
hello()

import json
student={
    "name":"John",
    "age":20
}
data=json.dumps(student)
print(data)


import json
data='{"name":"Disha","age":22}'
result=json.loads(data)
print(result["name"])

import requests

response=requests.get("https://api.github.com/users/python")

data=response.json()
print(data)