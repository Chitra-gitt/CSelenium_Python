'''
Created on 7 May 2025

@author: Chitra

Inheritance: carry forwarding properties from one class to another class

Parent/super class: from which class property is being inherited. (ex- male and female class)

Child/sub-class: To which class a property is being inherited (ex- male and female class)

from object perspective, an object created from a child class should be able to access/call the
properties from its parent class

Why we need inheritance?

- It reduces code repetition and increase code reusability which help us in easy maintenance.

Types of inheritance:
1. single level inheritance
2. Multi-level inheritance
3. Multiple inheritance


Method resolution order(MRO)- In an inheritance when we call a method using  an object,
MRO will help python interpreter to decide in which order it has to traverse the class.

"object class" is the super-class of all the classes in the python.



'''




class Grandfather:
    def __init__(self):
        print("This is grandfather class constructor")
        
    def gf_method(self):
        print("This is Grandfather method")
        
class Mother(Grandfather):
    def __init__(self):
        print("This is mother class constructor")
        
    def m_method(self):
        print("This is Mother class m_ method")
        
    def car(self):   
        print("This is mother's car")
class Father():
        
    def f_method(self):
        print("This is Father method")
        
    def car(self):   
        print("This is father's car")   
            
        
class Child(Mother,Father):
    def __init__(self):
        print("This is child class constructor")
        
    def c_method(self):
        print("This is Child class c_method")


print("==========Grandfather class==========")        
ajja=Grandfather()
ajja.gf_method()

print("==========Mother class==========")        
amma=Mother()
amma.m_method()
amma.gf_method()

print("==========Child class==========")        
baby=Child()
baby.c_method()
baby.gf_method()
baby.m_method()
baby.f_method()
baby.car()

print("=========This is Method resolution class(MRO)=========")
print(Child.mro())




