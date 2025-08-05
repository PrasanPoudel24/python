#oop -> programming paradigm based on the concept of program

#class , objects, methods, attributes , decorators, constructor, magic/dunder methods

#4 pillars -> inheritance, encapsulation, polymorphism, abstraction 

#class
"""

class ABC:
    #attributes,methods and constructor contains inside it
    name="prasan"
    age= 21
    gender="male"
    def data(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"gender: {self.gender}")
        
    def add(self,a,b):
        return a+b
    
one=ABC()#object

print(one.name)
one.name="ramu"
print(one.name)
print(one.age)
print(one.gender)

one.data()
print(one.add(9,19))


#wap to create a class named Car with attributes like name, model, year,
# and methods like start , stop ,and display_info




class Car:
    name=str(input("Enter car name:"))
    model=str(input("Enter car model:"))
    year=int(input("Enter car year:"))
    
    def start(self):
        print(f"CAR name {self.name} of model {self.model} made in year {self.year} is started")
    def stop(self):
        print(f"CAR name {self.name} of model {self.model} made in year {self.year} is stopped")
        
    def car_info(self):
        print("name :" ,self.name)
        print("model :" ,self.model)
        print("year :" , self.year)
        
        
new = Car()
new.car_info()
new.start()
new.stop()

#constructor

class xyz:
     def __init__(self,a,b):
         print("constructor is called")
         print(f"sum : {a+b}")

new1=xyz(9,10)

        






#wap to create a class named student with attribute like name ,age ,and 
# methods like study, attend_class and display_info using constructor


class Student:
    def __init__(self, name, age):
         self.name=name
         self.age=age
         print("valued added")
    def study(self):
        print(f"{self.name} is studying")
        
    def attend_class(self):
        print(f"{self.name} is attending class")
    
    def display_info(self):
        print(f"name : {self.name}  age: {self.age}")
        
a=str(input("enter your name: "))
b=int(input("enter your age: "))

new2=Student(a,b)
new2.attend_class()
new2.study()
new2.display_info()



#decorators in python -> @classmethod <@staticmethod ,@abstractmethod ,@property

class ones:
    two="class variable"
    def one(self):
        print(f"this is method one {self.two}")
        
    #class method
    @classmethod
    def twos(cls):
        print(f"class method : {cls.two}")
        
    #static
    @staticmethod
    def threes(a,b):
        print(f"static method : {a+b}")
    
     
ones.twos()
ones.threes(2,4)

#wap to create a class named student with attribute like name ,age ,and 
# methods like study, attend_class and display_info using decorator

class student:
    name="RAM"
    age=20
    @classmethod
    def study(cls):
        print(f"{cls.name} is studying")
        
    @staticmethod
    def attend(name):
        print(f"{student.name} is attending class")
        
    @classmethod
    def display(cls):
        print(f"name : {cls.name}  age: {cls.age}")
        
        
student.study()
student.display()
student.attend("hari")
"""

#FUNCTION DECORATOR

def add_five(func):
    def wrapper(*args,**kwargs):
        result =func(*args,**kwargs)
        return result + 5
    return wrapper

@add_five
def add_number(a,b,c):
    return a+b+c
print(add_number(10,1,12))

