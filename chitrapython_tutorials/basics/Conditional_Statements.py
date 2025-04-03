'''
Created on Mar 29, 2025

@author: Chitra

 conditional statements: statements which check the condition and determine the flow
 
 Types of conditional statements:-
 
1. If a condition is satisfied , then one set of code will be executes, otherwise the another set of code is executed.
 2.if else statements
 3. series if else statements
 4. nested if else statements 
 
 
 Syntax:
 
 IF condition:
 <code to be executed if condition is satisfied>
 
 Indentation 
 
 
if age>=18 and age<=59:
    print("Yor're and Adult")
    
elif age<18 and age>=12:
    print("Yor're an adolescent")
    
elif age<12 and age>=5:
    print("You're an Child")
    
elif age>=0 and age<4:
    print("You're an baby")

elif age>=60:
    print("You're an senior citizen") 
    
  
  


if age>=18:
    if age<=59:
        print("Yor're and Adult")
    else:
        print("You're an senior citizen")    
else:
    if age>=13:
            print("Yor're an adolescent")
    else:
        print("You're an Child")
        
    '''
             
         
age=int(input("Enter your age:"))    

if age>=0:
    if age in range(0,13):
        print("Child")
        
    elif age in range(13, 19):
        print("Adolescent")
    elif age in range(19,60):
        print("adult")
        
    else:
        print("senior citizen")
else:
    print("pls enter positive number") 
    
