'''
Created on Apr 1, 2025

@author: Chitra

Looping statements: Statements which executes a code multiple times until a required condition is satisfied.

Types-
1) while loop-

a. initialising of variable
b.while condition>>while block
c. increment/decrement

2) for loop- iterate over collections/range

a. 

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

 
 
 
 
count=0
while count<=100:
    if count==50:
        count+=1
        continue
    print(count)
    count+=1
     
     
#print (range(10))

for n in range(1,100):
    if n==50:
     continue
    print(n)
    
    
    
for n in range(1,100):
    if n%2==0: #even numbers
    #if n%2==1: #odd numbers
        if n==90:
            continue
        print(n)
    
    
for n in range(0,100,2):
    print (n)   
    
    
    
for n in range(5):
    print("*", +1)
    
    

for n in range(1,6):

    for m in range(6-n):
        print("*", end=" ") #end is used to type in next line
        
    print()
    
    o/p-
    
* 
* * 
* * * 
* * * * 
* * * * * 


    
for n in range(6,0,-1):

    for m in range(n):
        print("*", end=" ") #end is used to type in next line
        
    print()
    
    o/p-
    
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

No. of stars(5)=stop value-row no.
   
for n in range(1,6):

    for m in range(n):
        print(" * ", end=" ") #end is used to type in next line
        
print()
    

  #UPWARD RIGHT ANGLE TRIANGLE
   
for n in range(1,6):

    for m in range(n):
        print("*", end=" ") #end is used to type in next line
        
    print()
   
   
   #DOWNWARD RIGHT ANGLE TRIANGLE
for n in range(1,6):

    for m in range(6-n):
        print("*", end=" ") #end is used to type in next line
        
    print()
   
  
    #UPWARD PYRAMID
    
for n in range(1,6):
    for m in range(6-n):
        print("", end=" ") 
        
    for i in range(n):
        print("*", end=" ")
        
    print()
   
   o/p-
   
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 

   '''
   
   
   
   
   
   
   
   
   
   
    
    
    