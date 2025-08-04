


list1=[1,2,3,4,5]



#power
output1=[i*2 for i in list1]
print(output1)

#even
output2=[ j*2 for j in list1 if j % 2 ==0]
print(output2)

#wap to print the square of even numbers from 1 to 100

output3=[ k*2 for k in range(101) if k % 2 == 0]
print(output3)


#wap to print the multiplication table of 7 using list comprehension

output4=[(7*i) for i in range(1,11)]
print(output4)


#wap to print the square of prime numbers from 1 to 100

output5=[i*2 for i in range(15) if ((i % i)==0 and (i % 1)==0)]
print(output5)



