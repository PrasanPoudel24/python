#abstraction in python -> hiding complex logic from user
"""
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



from abc import ABC,abstractmethod

class teahouse(ABC):
    def process_complete(self):
        self.order()
        self.adding_materials()
        self.serve()
    
    @abstractmethod
    def order(self):
        pass

    @abstractmethod
    def adding_materials(self):
        pass
    
    @abstractmethod
    def serve(self):
        pass
    
    
class milktea(teahouse):
    def order(self):
        print("ording milk tea")
        
    def adding_materials(self):
        print("Adding milk, sugar and tea leaves")
     
    def serve(self):
        print("serve in ceramic cup")
        
class blacktea(teahouse):
    def order(self):
        print("ordering black tea")
        
    def adding_materials(self):
        print("Adding water, sugar and tea leaves")
        
    def serve(self):
        print("serve in glass cup")




user1=milktea()
user1.process_complete()
user2=blacktea()
user2.process_complete()



from abc import ABC, abstractmethod

class cafe(ABC):
    def process_end(self):
        self.cafe_lattee
        self.cafe_cappuccino
        self.cafe_americano
        self.cafe_mocha
        self.cafe_espresso
    def cafe_lattee():
        pass
    def cafe_cappuccino():
        pass
    def cafe_americano():
        pass
    def cafe_espresso():
        pass
    def cafe_mocha():
        pass
    
class User1(cafe):
    pass

class User2(cafe):
    pass




#Polymorphim


class animal:
    def eat(self):
        print("Eating...")

class lion:
    def eat(self):
        print("lion is eating")
        
class tiger:
    def eat(self):
        print("tiger is eating")
        
obj1=animal()
obj2=lion()
obj3=tiger()

for i in (obj1,obj2,obj3):
    i.eat()


"""


























