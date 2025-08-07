#errorhandling and exception handling
#try , except ,finally
"""
print("hi")
try:
    a=int(input("enter a number: "))
    print(10/a)
#except ZeroDivisionError:
 #   print("you can't divide by zero")
    
    
except Exception as e:
    print(e)#RUN WHEN THERE IS EXCEPTION
    
else:
    print("hello world works successfully")#RUNS WHEN THERE IS NO EXCEPTION
    
finally:
    print("this is finally block")#runs in any case whether exception is there or not
    
    
print("hello world")
"""


#try , except ,finally
def fun():
    
    try:
        num=int(input("enter number: "))
        if num%2!=0:
           print("odd")
        else:
           print("even")
    except Exception as e:
        print(e)
    
fun()

