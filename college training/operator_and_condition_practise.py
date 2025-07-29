"""
#arthimetic operator
x=5+6

print(x)

print(4*5)

print(6-2)

print(10/2)

print(10%2)

print(4**3)#power

print(5//5)#


#wap to print the sum of two number by asking user to input the number

x=input("enter a number: ")
y=input("enter a number: ")

print("sum of two number is:",x+y)
print(f"the sum is {x+y}")



#wap the program for the dollar conversion

print("Your conversion rate is 130")
x=float(input("enter amount in dollar: "))
print( x * 130," is the value into nepali rupees")



#assignment operator

a=10
b=a
c=b
print(a,b,c)

a -= 10
print(a)

b *=c
print(b)

c **=2
print(c)



#comparision operator

a=45

b=45
print(a==b) #true
print(a!=b) #false
print(a>b) #false

c=23
print(a>c) #true

print(a>=b)


#logical operator

print(True and False)
print(True and True)
print(False and False)
print(False and True)


print(True or False)
print(True or True)
print(False or False)
print(False or True)

print(not True)
print(not False)



#identify operator


a= 30
b=30
c=45

print(a is b)
print(a is c)
print(a is not b)
print(a is not c)



#Membership operator

list1=[1,2,3,4]
print(1 in list1)
print(2 not in list1)




# bitwise operator
print(5&5) 
print(5&4)
print(5|5)
print(5|4)





#ternary operator
a=10
b=20
print("above 18" if(a>18) else "below 18")
print("above 18" if(b>18) else "below 18")




#wap a program to print the nu,ber is odd or not by asking input from the user 

x=int(input("enter a number: "))

    
print("is odd" if x%2!=0 else "is even")

    
    
    
#wap to print if the user can drive or not
age=int(input("enter your age: "))
print("can drive" if age>18 else "cannot drive")  



#condition in python

#if, else, elif, match
value=int(input("enter a number:"))
if(value%2==0):
    print("value is even")
    
elif(value%2!=0):
    print("value is odd")
    
else:
    print("num is zero")



#wap to print if the given value id fizz, buzz or fizzbuzz conditios are
#fizz -> nmber divide by 3
#buzz -> number divide by 7
#fizzbuzz -> number divide by both 3 and 7


value=int(input("enter a number: "))
if(value==0):
    print("entered value is zero")
elif(value%3==0):
    print("fizz")
    
elif(value%7==0):
    print("buzz")
    
elif(value%7==0 & value%3==0):
    print("fizzbuzz")
    
else:
    print("value doesnot match the above conditions")
    
 """  
 
#match 
day=str(input("enter a day: "))
match(day):
    case 'sunday':
        print("sunday")
        
    case 'monday':
        print("monday")
        
    case 'tuesday':
        print("tuesday")
        
    case _:
        print("none")


