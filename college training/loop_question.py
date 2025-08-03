"""#wap to print the eve numbers from 0 to 100

for i in range(0,100,2):
    print(i)
#wap to print the all th prime number from 0 to 100

for i in range(1,100):
    if(i/1==0 and i/i==0):
        print("prime number: ", i)
        
    else:
        print("not prime number: ", i)
    
#wap to print multiplicationtable of 7


for i in range(1,11):
    print(f"7 * {i} :{i*7}")
    

        

# wap to print the fibonacci series to 10 items

a=0
b=1
print(a)
print(b)
for i in range(1,11):
    c=a+b
    print(c)
    a=b
    b=c
    

   
   
#wap to print the sum of all the numbers from 0 
num1=0
for i in range(1,11):
    num1 +=i
print(num1)
#wap to print the fizz if number is divisible by 3,buzz if divisible by  5,fizzbuzz if divisible by both 3
# and 5
 
for i in range (0,100):
    if(i==0):
        print("zero",i)
    elif(i%5==0):
        print("buzz",i)
    elif(i%3==0):
        print("fizz",i)
    elif (i%5==0 and i%3==0):
        print("fizzbuzz",i)
    else:
        print("not divisible",i)
#wap to print the reverse of number 


x=int(input("enter a number: "))
y=str(x)
v=y[::-1]

print(int(v))


# wap to print the factorial of a number of your choice
fact=1
num=int(input('enter number: '))
if num==0:
    print(0)
elif num==1:
    print(1)
else:
    for i in range(1,num+1):
      fact*=i
    print(fact)"""
    
    
    
    
#wap to print this star pattern also in reverse
#*
#**
#***
#****
#*****

for i in range(1,6):
    print("*"*i)
              