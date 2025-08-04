#calculator app using fun -> add ,sub ,dev,mul,**,//,% and ask the # input for the user 2 will be numbers 
# and 1 will be option and use recursion to call the function again and again until the user wants to exit
"""
def add(x,y):
    print(f"Sum of the numbers is : {x+y}")
    
def sub(x,y):
    print(f"Subtraction of the numbers is : {x-y}")
    
def div(x,y):
    print(f"division of the number is : {x/y}")
    
def mul(x,y):
    print(f"Multiplication of the numbers is : {x*y}")
    
def p(x,y):
    print(f"** of the number is {x**y}")
    
def d(x,y):
    print(f"// of the number is {x//y}")


        
def calculator():
    print("MENU")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Division")
    print("4.Multiplication")
    print("5. **")
    print("6. //")
    print("7. exit")
    
    a=int(input("enter which operation you want to perform: "))
    
    match a:
        case 1:
            x=int(input("enter first number: "))
            y=int(input("enter second number: "))
            add(x,y)
            rec()
            
        case 2:
            x=int(input("enter first number: "))
            y=int(input("enter second number: "))
            sub(x,y)
            rec()
            
        case 3:
            x=int(input("enter first number: "))
            y=int(input("enter second number: "))
            div(x,y)
            rec()
            
        case 4:
            x=int(input("enter first number: "))
            y=int(input("enter second number: "))
            mul(x,y)
            rec()
            
        case 5:
            x=int(input("enter first number: "))
            y=int(input("enter second number: "))
            p(x,y)
            rec()
            
        case 6:
            x=int(input("enter first number: "))
            y=int(input("enter second number: "))
            d(x,y)
            rec()
        
        case 7:
            print("program terminate")
            return 
        
        case _:
            print("invalid input")
            return 
            
            
def rec():
        calculator()
    
        
rec()   
"""   

#wap to print factorial of a number using recursion

def rec1(n):
    if n==0 or n==1:
        return 1
    else:
        return n*rec1(n-1)
    
num=int(input("enter a number: "))
a=rec1(num)
print(f"factorial of {num} is {a}")