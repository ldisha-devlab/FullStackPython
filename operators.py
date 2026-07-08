# #Operators
product_price=5000
delivery_charge=500
total=product_price + delivery_charge
print(total)


a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

student =10
groups=2
print(student // groups)

# # Assignment Operators
followers=100
followers=followers+1
print(followers)
followers-=1
print(followers)

# #Comparison Operators

saved_password="1234a"
entered_password="123abcd"
print(saved_password == entered_password)


# #logical operator

balance=1200
pin_correct=True
if balance>=1000 and pin_correct:
    print("withdraw allowed")
else:
    print("failed")

# #Simple Program
product=input("Enter product name:")
price=int(input("Enter the price:"))
quantity=int(input("Enter the quantity:"))
discount=int(input("Enter the discount:"))
total=price*quantity
final_bill=total-discount
print("Product:",product)
print("Total Amount:",total)
print("Final Bill:",final_bill)

# #Conditional Statements

password=input("Enter the password:")
if password == "admin123":
    print("Welcome")
else:
    print("wrong password")

 #Simple Program
SGPA=int(input("Enter current semester SGPA:"))
if SGPA>=9:
    print("A grade")
elif SGPA>=7:
    print("B grade")
elif SGPA>=6:
    print("C grade")
else:
    print("fail")

# #Logical Operator

# # and Operator
age =30
salary=50000
if age>=18 and salary >=30000:
    print("You are eligible for the loan")

# # or Operator

day ="Sunday"
if day=="Sunday" or day =="Saturday":
    print("Holiday")

# #not Operator

statement="It is raining"
print(not(statement))

login = False

if not login:
    print("print Login")

#Simple Program
def with_draw():
    pin=int(input("Enter the pin:"))
    secret_pin=1234
    total_amount=50000
    if pin==secret_pin:
        amount=int(input("Enter the amount to withdraw:"))
        if amount<total_amount:
            print("Successful Withdraw of Rs.",amount)
            check_balance=total_amount-amount
            print("Balance:",check_balance)
        else:
            print("Insufficient Balance")
    else:
        print("Incorrect pin code")
with_draw()

# for Loop
for i in range(2,6):
    print(i)
    
users=["user1","user2","user3"]
for user in users:
        print("Mail sent to",user)  
print("Batch completed")


name="Dhoni"
for ch in name:
    print(ch)


number=1234
for i in str(number):
    print(i)

#While Loop
count=1
while count <=5:
    print(count)
    count+=1    

count=5
while count>=5:
    print(count)
    count-=1   

for i in range(5):
    if i==3:
        break
    print(i)

for i in range(2,6):
    if i==4:
        continue
    print(i)

for i in range(2,6):
    if i==4:
        break
    print(i)


password=""
while password!="admin123":
    password=input("Enter the password:")
print("Welcome")


student1="ram"
print(student1)
student2="sam"
print(student2)

# List Operations
List=["paste","brush","soap"]
List.append("shampoo")
print(List)
List.insert(2,"loofah")
print(List)
List.remove("soap")
print(List) 


