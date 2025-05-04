'''

Created on 25 Apr 2025

@author: Chitra

Reverse a String Without Using Slicing*
Use a loop to reverse a given string (e.g., `"hello"` → `"olleh"`).
 '''       


a='hello'
print("hello")

for b in a:
    b== a-1:
        print('b')
        
    
    
a=''
for b in a:
    a=b+a
#return a

print(a('hello'))
'''
'''
from _operator import index

#using slicing operator

a='hello'
b=a[ ::-1]
print(b)

#without using slicing operator

name="lakshmi ganesha"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

print("Negative index")
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])

index=-1
reverse_string=""
while index> -6:
    reverse_string=reverse_string+name[index]
    index=index-1
print(reverse_string)


print(len(name))
index=-1
reverse_string=""
while index> -(len(name)+1):
    reverse_string=reverse_string+name[index]
    index=index-1
print(reverse_string)


'''

Check if a Number is Prime*
Write a loop to check if a given number is a prime.

'''

for n in range(1,100):
    if n%1==0: #prime numbers
        print("prime number")
    
print(n)


print('-----------------------------------------------------------------------------------')

for n in range(1,100):
    #if n%2==0:
        #print("even number-->",n) #even numbers
    #elif n%2==1:
        #print("odd number-->",n) #odd numbers
        if n%2!=0:
            print("prime number-->",n)   
#elif n==90:
        #continue
          
print('-------------------------------------------------------------------')
 
   '''  

Check if a String is a Palindrome Using a Loop*
Input: 
Ex:
`"madam"` → Output: `True`
'''

#name1='madam'
reverse_string= " "
names=reverse_string-names
names= input("enter name:")
if names==names:
    print("String is a palindrome")
else:
    print("Not palindrome")
    