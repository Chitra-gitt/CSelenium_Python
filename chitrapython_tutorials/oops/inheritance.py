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
object class object() is parent class of all the classes.

super class keyword- super() is used to call super class/ parent class constructors 
or methods to child class when there is a constructor or method present in child class with same 
name as super class.
'''


class GrandFather:
    def __init__(self, name):
        print("`object is created with name:", name)
        
    def gf_method(self):
        print("This is Grandfather method")
        
class Mother(GrandFather):
    def __init__(self, name, age):
        #print(f"This is mother name: {name}, age: {age}")
        super().__init__(name)
        print(f"Age of {name} is {age}")


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
#     def __init__(self):
#         print("This is child class constructor")
        
    def c_method(self):
        print("This is Child class c_method")


print("==========Grandfather class==========")        
ajja=GrandFather("tatha")
# ajja.gf_method()

print("==========Mother class==========")        
amma=Mother("amma", 55)
# amma.m_method()
# amma.gf_method()

print("==========Child class==========")        
baby=Child("baby", 32)
# baby.c_method()
# baby.gf_method()
# baby.m_method()
# baby.f_method()
# baby.car()

print("=========This is Method resolution class(MRO)=========")
print(Child.mro())

print("=========Directory method(dir)==========")
print(dir(baby))

