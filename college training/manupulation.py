#string manupulation

"""

name="prasan poudel"

print(name)
print("RAM \n BAHADUR")
print("RAM\\BAHADUR")
print("RAM\tBAHADUR")

print("hi's my name is prasan poudel")

print('hi\'s my name is prasan poudel')

#slicing

print(name[0])
print(name[0:7])
print(name[0:6:1])
print(name[-1:-6:1])

print(name[::-1])#reverse the string

#strimg method

d="hello world"
f="   HELLO WORLD"
g="helloworld"
print(d.upper())
print(f.lower())
print(g.capitalize())
print(d.title())
print(f.strip())#extra space lai udauxa
print(d.replace("hello","HELLO"))
print(f.find("WOR"))
print(d.isupper())
print(d.islower())
print(f.istitle())
print(f.isalpha())#if space contains then it gives false
print(g.isalnum())#false contains numbers and letters but also space




\




#wap to print if the given value is palindrome or not

x=str(input("enter a word: "))

y=x[::-1]
if x==y:
    print("the given word is pallindrome")
    
else:
    print("the given number is not pallindrome")
    
    
   
#list in python (methods)


list1=[1,2,3,4,5]
#index and length contains by default
print(list1)
#methods


print(list1.index(5))

list1.append(6)#last ma value add garxa

print(list1)

list1.insert(0,7)#first is index and second is the value
print(list1)

list1.pop()#remove last index
print(list1)


list1.remove(7)
print(list1)

list1.reverse()
print(list1)

list2=[9,6,4,5,3,4,1,8,7]
list2.sort()#sort the list in ascending order
print(list2)

list2.sort(reverse= True)#sort the list in descending order
print(list2)

 
 
 
 #tuple methods
 
tuple1=(1,2,3,4,5)
print(tuple1)

print(tuple1.count(3))#count the number of repeatation

print(tuple1.index(3))# send the index of the number

#wap to add items in tuple by converting the tuple to list use append to add the item the provide me 
#value in tuple
tup2=(1,2,3,4)
print(tup2)
li1=list(tup2)

li1.append(5)

tup2=tuple(li1)
print(tup2)

# for loop in list and tuple

for i in tup2:
    print(i)
    
for i in li1:
    print(i)



#set methods
set1={1,2,3,4,5,6,7,8}
set2={5,2,3,6,8,9}
print(set1)

#list1.clear() provide khali space
set1.add(10)
print(set1)

set1.remove(10)
print(set1)

set1.pop()
print(set1)

set3=set1.union(set2)

print(set3)

set4=set1.intersection(set2)

print(set4)

set5=set1.difference(set2)
print(set5)

set5.clear()
print(set5)

set1={1,2,3,4,5,6,7,8}
set2={5,2,3,6,8,9}
print(set1&set2)

print(set1|set2)

"""

#wap to print the union items in the set
list1=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5]
se1=set(list1)

se2=se1.intersection()
print(se2)