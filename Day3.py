students={"Alice","Bob","Charlie"}
print(students)
numbers={1,2,3,4,5}
print(numbers)

# Tuples is a collection which is ordered and unchangeable. Allows duplicate members.it is used to store values in a single variable. Tuples are written with round brackets

students=("Alice","Bob","Charlie")
numbers=(1,2,3,4,5)

print(students[-2])
print(numbers[-3])

#data=(1,2,3)    
#data[0]=200 
#print(data)  #Exception because tuple is immutable

x=(1,2,3,1,2,2,1,1,1,6,7,1)
print(x.count(1))
print(x.count(6))

items=("soap","paste","shampoo","soap","paste")
print(items.count("soap"))
print(items.count("shampoo"))


print(items.index("soap"))
print(items.index("shampoo"))
print(items.index("paste"))

num=(10,20,30,40,50)
print(num[1:4])
print(num[:2])

# num={1,2,3,4,5,1,1,1,1,1}
# print(num.index(1)) #Exception because set doesn't allow duplicate values

#Set is unordered it does'nt allow duplicate values it stores unique values
 
num={1,2,3,4,5,1,1,1,1,1}
print(num)  # Output:{1,2,3,4,5} 

#sets
num={1,2,3,4,5,1,1,1,1,1}
data={1,2,3}
data.add(4)
print(data)

a={1,2,3}
b={3,4,5}
print(a|b) #Union Output:{1,2,3,4,5}
print(a&b) #Intersection Output:{3}

"""Function is reusable block of code that used to perform specific task"""

def greeting():
    print("Hello Friends!!!!!!!!!!!!!!!!!!!!")
greeting() #Output:Hello Friends!!!!!!!!!!!!!!!!!!!!

def add(a, b):
    return a + b
print("Addition:",add(10, 20))  # Output: Addition:30

def multiply(a, b):
    return a * b
print("Multiplication:",multiply(17, 23))  # Output: Multiplication:391

def subtract(a,b):
    return a-b
print("Subtraction:",subtract(1000,2000)) #Output:  Subtraction:-1000

def divide(a,b):
    return a/b
print("Division:",divide(1000,2000)) #Output:  Division:0.5

def modulo(a,b):
    return a%b
print("Modulo:",modulo(10,3)) #Output:  Modulo:1

def add(*num):
    total=0
    for i in num:
        total+=i
    print(total)
add(10,20,30,40,50,60)



def student(**details):
    print("name:",details["name"])
    print("age:",details["age"])
    print("job:",details["job"])
student(
    name="Disha",
    age=20,
    job="sales"
)

def square_root(n):
    return  n **0.5
print(square_root(49)) #Output:7.0

def square(n):
    return  n *n
print(square(49)) #Output : 2401

square=lambda x:x*x
print(square(25)) #Output:625

add=lambda a,b:a+b
print(add(10,20)) #Output:30

odd=lambda a:a%2!=0
print(odd(4))                   #Output:False
even=lambda b:b%2==0
print(even(3))                  #Output:False

num=lambda x:"Even" if x%2 == 0 else"odd"
print(num(10))
print(num(3))        # Output: Even odd

#Uppercase
string=lambda x:x.upper()
print(string("hello"))       #Output: HELLO


string=lambda x:len(x)
print(string("hello"))        # Output: 5



# File handling

file = open("student.txt", "a")
file.write("\nHello Friend!!!!")
file.close()
print("Data written successfully")

file = open("student.txt", "r")
data = file.read()
print(data)
file.close()      #Output: Hello Friend!!!!

file = open("student.txt", "a")
file.write('\n Hello Student')
file.close()
print("Data written successfully")

file = open("student.txt", "r")
data = file.read()
print(data)
file.close()                                   #Data written successfully        Hello Friend!!!!     Data written successfully      Hello Friend!!!!  Hello Student

#Exception Handling

try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

try:
    num=int(input("Enter a number:"))
    print(num)
except ValueError:
    print("only number allowed")

try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Enter only numbers")    
finally:
    print("Program Completed")

try:
    print(10/2)
except:
    print("Error")
else:

    print("success")