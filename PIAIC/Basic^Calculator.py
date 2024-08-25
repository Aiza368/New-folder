# 01
print(eval(input("enter your expression")))
#02
a=float(input("first value:"))
b=float(input("second value:"))
opr=input("operations: +,-,*,/")

if opr== "+" :
    print (a ,"+",b , "=" ,a+b)
if opr== "-":
    print (a ,"-",b , "=" , a-b)
if opr== "*":
    print (a ,"*",b , "=" , a*b)
if opr== "/":
    print (a ,"/",b , "=" , a/b)
if opr !="+"and opr !="-"and opr !="*"and opr !="/":
    print("invalid operation")
# 03
v1=float(input("Enter your first value:"))
v2=float(input("Enter your second value:"))
opr=input("operations:+,-,*,/")

if   opr== "+": 
    print(v1,"+",v2,"=",v1+v2)
elif opr=="-": 
    print(v1,"-",v2,"=",v1-v2)
elif opr=="*": 
    print(v1,"*",v2,"=",v1*v2)
elif opr=="/": 
    print(v1,"/",v2,"=",v1/v2)
else:
    print("Invalid operation")
 
