'''
Created on 3 May 2025

@author: Chitra


Arguments = Parameters

Types of arguments:
1. Formal arguments: parameters which are declared while defining a function.
    - Formal arguments collects/ accepts values(actual arguments) when a function is called
2. Actual arguments: actual values passed while calling a function

Ex: 
def addition(a, b): # a, b are formal arguments
    c=a+b
    return c
    
d=addition(10, 20) # 10, 20 are actual arguments
print(d)

Types of Actual arguments:
1. Positional arguments:
    - Actual arguments which are assigned to formal arguments based on their positions
2. Keyword arguments:
    - Actual arguments which are assigned to formal arguments using key-value pair


Types of formal arguments:

1) Default arguments- declaring and defining values for the variable is default argumet
ex- e-m*c**2


2)variable length arguments-  use '*' -  in the form of tuple ()-accepts variable number of arguments. ex-0,1,2,3,...

3) keyword variable arguments- syntax is '**' , stores value in dictionary type with {}




'''
def subtraction(a, b):
    c=a-b
    print("a=", a)
    print("b=", b)
    print("c=", c)

# subtraction(20, 10) # a= 20; b= 10
# subtraction(10, 20) # a= 10; b= 20
# subtraction(b=10, a=20)

#E=M*C**2

def cal_energy(m, c=300000000):
    e=m*c**2
    print("energy in joules-->",e)
    
    
# cal_energy(5)   
# cal_energy(3) 

#def addition(a,b):
#   c=a+b
#  return c


def addition(*a):  # '*' is symbol of variable argument
    print(sum(a))
    #print(type(a))

# addition()
# addition(1,)
# addition(6,5)
# addition(6,7,8,9)

b= (3,4,5,6,7) #using for loop


def display(**x):
    print(x)
    
#display(name= 'chitra', age= 33, gender= 'female')
