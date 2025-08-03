#function in python
#def 

#return statement
"""
#function typesreturn, no return -> 4
#no parameter , no return
def hello(): 
    print("Hello, World!")
    
print(hello())
#no parameter , return
def getinfo():
    return f"hello world{name}"

x=getinfo()
print(x)
#parameter , no return

name="prasan"
def new(name):
    print(f"Hello, {name}")

print(new(name))
#parameter , return

def add(a,b):
    return (a+b)

x=add(5,8)
print(x)


#parameter type in function 
#1. default parameter

def defaultpara(a = 0,b=30):
    print (a+b)
defaultpara()
defaultpara(10)
defaultpara(20,60)


#WAP to print the power of two numbers using default parameter

def power(a=9,b=2):
    print(a**b)
power()
power(7)
power(6,3)




#2. positional parameter
def normalFun(name,age):
    print(f"my name is {age} and age is {name}")
    
normalFun("ram",19)

#3. named / keyword parameter

def Fun(name,age):
    print(f"my name is {age} and age is {name}")

Fun(45,"ram")





#3.* args parameter
def abc(a,b,*args):#takes multiple arguments
    print(a)
    print(b)
    print(args)
    
abc(10,20,84,45,262,462)




#4. **kwargs parameter

def xyz(**kwargs):
    print(kwargs)
    
xyz(name="shyal",age=21,add="jhapa")


#wap to use all the parameter types in a single function


def start(a=7,b=18,c=23):
    print(a+b+c)

start(20)
start()
start(6,7,9)

def next(kilometer,road):
    print(f"you travelled {road} km in {kilometer} road ")
    
next(56,"BP highway")
next("BP highway",56)




def third(c,*args):
    print(c)
    print(args)



third(13,45,67,12,78,25,75,63)


def last(**kwargs):
    print(kwargs)
    
last(name="ashim",age=20,address="kathmandu")




def double(*args,**kwargs):
    print(args)
    print(kwargs)


double("name","age","address",name="ashim",age=20,address="kathmandu")




def abcd(a,b,c,*args,**kwargs):
    print(f"a: {a}, b:{b},c:{c}")
    print("Additional args: ",args)
    print("keyword args: ",kwargs)
    
abcd(10,20,30,40,50,name="hari",age=25,gender="male")

#anonymus function /lamda function

x= lambda : 22
print(x())

adds = lambda a,b: a+b
print(adds(10,20))




#wap to print the given value is even or odd using lambda function
A=int(input("enter a number: "))
a= lambda x: print("is even" if x%2==0 else "is odd")

a(A)

"""
#recursion -> function calling itself

def rec(n):
    if n==0:
        return 0
    else:
        return n + rec(n-1)
#996
print(rec(10))

