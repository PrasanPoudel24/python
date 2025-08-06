
"""
def exponents(func):
    def wrapper(*args,**kwargs):
        result =func(*args,**kwargs)
        return result ** 5
    return wrapper
@exponents
def calculate(a,b):
     return(a+b)
print(calculate(3,5))


# @property -> use for the lastname and firstname = fullname

class person:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
        
    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
    
obj1 = person("prasan","poudel")

print(obj1.firstname)
print(obj1.lastname)
print(obj1.fullname)








# 4 pillars of OOP -> encapsulation, inheritance , abstraction and polymorphism

#inheritance

class parent:
    def __init__(self,lname):
        self.lname=lname
    def hello(self):
        print("Hello from parent class", self.lname )
        
class child(parent):
    def __init__(self,name,lname):
        self.name=name
        super().__init__(lname)#parent ko lname lai grab garera rakheko xa
    def hlo(self):
        print("hello from child", self.name)
        
obj1=child("prasan","poudel")
obj1.hello()
obj1.hlo()
     
        
    
   



#encapsulation 
#hi -> "hello" #public
#_hi ->"hello" #protected
#__hi ->"hello" #private


class Bank:
    def __init__(self,name,balance):
        self._name=name
        self.__balance=balance
        
    @property
    def getbalance(self):
        return self.__balance
    
    @getbalance.setter
    def setbalance(self,balance):
        self.__balance=balance
        
    def __calculateminbalance(self):
        if self. __balance > 500:
            print("hello")
            
    def calling(self):
        self.__calculateminbalance()
        
obj1= Bank("prasan",89765)
print(obj1._name)    
print(obj1.getbalance)
obj1.setbalance=3000
print(obj1.getbalance)
obj1.calling()



#abstraction in python -> hiding complex logic from user

from abc import ABC, abstractmethod
class Coffee(ABC):
    def makeCoffee(self):
        self.gason()
        self.addCoffee()
        self.addMaterials()
        self.servein()

    @abstractmethod
    def gason(self):
        pass
    @abstractmethod
    def addCoffee(self):
        pass
    @abstractmethod
    def addMaterials(self):
        pass
    @abstractmethod
    def servein(self):
        pass

class Espresso(Coffee):
    def gason(self):
        print("coffee machine on")
    def addCoffee(self):
        print("addCoffee beans and exxtract it")
    def addMaterials(self):
        print("water, sugar and milk")
    def servein(self):
        print("serve in cup")
    
class Cappuccino(Coffee):
    def gason(self):
        print("coffee machine on")
    def addCoffee(self):
        print("extracted coffee powder")
    def addMaterials(self):
        print("water, sugar and milk")
    def servein(self):
        print("serve in cup")

exp = Espresso()
exp.makeCoffee()

cap = Cappuccino()
cap.makeCoffee()
""" 




# wap to create a parent class named Classes with attribute like class_name section and have to inherit it to child class named Students with attributes like name, age, and methods like study, attend_class, and display_info using constructor and use super() to access parent class attributes and methods

class classes:
    
    def __init__(self,class_name,section):
        self.class_name=class_name
        self.section=section
    
    
    
class students(classes):
    def __init__(self,name,age,class_name,section):
        self.name=name
        self.age=age
        super().__init__(class_name,section)
        
    def study(self):
        print(f"Name: {self.name} study in class = {self.class_name}")
        
    def  attend_class(self):
        print(f"Name: {self.name} attend in class = {self.class_name}")
        
    def display_info(self):
        print(f"Name: {self.name} class = {self.class_name} age = {self.age} section = {self.section}")
        
        
obj=students("prasan",11,"Seven","A")
obj.attend_class()
obj.display_info()
obj.study()