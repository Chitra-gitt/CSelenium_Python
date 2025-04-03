'''
Created on Apr 1, 2025

@author: Chitra

Looping statements: Statements which executes a code multiple times until a required condition is satisfied.

Types-
1) while loop-
a. 
2) for loop

Loop control statement:
1. Break statement- stops loop execution at one point of time
2.continue statement- skips the execution of loop for once

*Pass statement- 

count=0

while count<5:
    
    print("Hi Chitra")
    count=count+1 #count+=1 this code can also be used . this is increment operator: +=, decrement operator: -=;
    
count=5

while count>0:
    
    print("Hi Chitra")
    count=count-1
    
    
while True:
    a=input("Enter a number1:")
    b=input("Enter a number2:")
    
    c=float(a)
    d=float(b)
    
    print(f"Addition of {c} and {d}:", c+d)
    e=input("Do you wish to continue?(Y/N):")
    if e=='N':
        break

 '''
 
 
 
count=0
while count<=100:
    if count==50:
        count+=1
        continue
    print(count)
    count+=1
     