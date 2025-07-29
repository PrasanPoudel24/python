# Write a Python program to check if a number is even or odd using an if-else statement.

x=int(input("enter a number: "))
if x%2!=0:
    print("number is odd")
    
else:
    print("number is even")

    
# Ask the user for their age and print whether they are eligible to drive (age >21) using a conditional expression.
 

 
age=int(input("enter your age: "))

if age>18:
    print("You are eligible for driving")
    
else:
    print("You are not eligible to drive")







# Write a program to check if a number is divisible by both 3 and 7 (fizzbuzz)using if-elif-else.

valuea= int(input("Enter a number: "))

if valuea == 0:
    print("Entered value is zero")
    
elif valuea % 3 == 0 and valuea % 7 == 0:
    print("fizzbuzz")
    
elif valuea % 3 == 0:
    print("fizz")
    
elif valuea % 7 == 0:
    print("buzz")
    
else:
    print("Value does not match the above conditions")
    
    
# Use a match statement to print the name of the day based on user input (e.g."sunday", "tuesday", etc.). 

day=str(input("enter a day: "))
match(day):
    case 'sunday':
        print("sunday")
        
    case 'monday':
        print("monday")
        
    case 'tuesday':
        print("tuesday")
        
    case 'wednesday':
        print("wednesday")
        
    case 'thursday':
        print("thursday")

    case 'friday':
        print("friday") 
        
    case 'saturday':
        print("saturday")       
    case _:
        print("none")


# Write a program to check if a number is positive, negative, or zero using if-elif-else.

x=int(input("Enter a number: "))

if x==0:
    print("the number is zero")
    
elif (x>0):
    print("the number is positive")
    
else:
    print("the number is negative")
    
 # Ask the user for a number and print "High" if it is above 90, "Zero" if it is
    #0, or "Other" otherwise.
    
num1=int(input("enter a number: "))

if num1>90:
    print("high number")
    
elif(num1==0):
    print("number is zero")
    
else:
    print("other")
    

 # Write a program to check if a value exists in a list using the in operator and print a message.
 
list1=[1,3,5,7,9,11,17]
print(4 in list1)

print(7 in list1) 
 
 
 # Demonstrate the use of arithmetic operators by calculating the sum, difference, product, and quotient of two numbers.
 
 
x=input("enter a number: ")
y=input("enter a number: ")

print("sum of two number is:",x+y)
print("the sum is ",(x+y))



#wap the program for the dollar conversion

print("Your conversion rate is 130")
x=float(input("enter amount in dollar: "))
print( x * 130," is the value into nepali rupees")
 
 
 
 # Show how to use assignment operators (+=, -=, *=, etc.) with an example.
 
a=90
b=80
c=70


a+=10
print(a)


b -=10
print(b)

c*=10
print(c)



 
 # Write a program to demonstrate the use of logical operators (and, or, not) with  boolean values.
 
print("USING AND") 
print(True and True)
print(True and False)
print(False and True)
print(False and False)


print("USING OR")
print(True or False)
print(True or True)
print(False or False)
print(False or True)


print("USING NOT")

print(not True)
print(not False)





