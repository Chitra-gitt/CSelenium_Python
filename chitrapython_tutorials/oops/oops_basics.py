'''
Created on 4 May 2025

@author: Chitra

Methods- are functions which are defined inside a class.
we can call methods using objects of that class


A method of one class can be called using an obj of the class

Constructor(__init__): It is a magic method used to construct an object,
by initializing it with specific values while creating the object.


Method Resolution Order(mro): 

Constructor(__init__): 

- It is a magic method used to construct an Object by initializing it with
specific values/ features being passed while creating the object.

- It is not mandatory to define a constructor. But when constructor is not defined interpretor 
will have its own constructor created

- Calling the constructor: 
    > Constructor is called implicitly during the creation of object
    > Still we can call constructor explicitly


Types of variables:

1) Method variables/local variable
2) object variable/instance variable
3) Class variable/static variable 

Major concepts of OOPS:

1)inheritance
2)Polymorphism
3)Abstraction
4)Encapsulation


'''


class SolarSystem():  '''defining class SolarSystem'''
    #Camel casing word- 1st letter is capital of each word
    def __init__(self,name):   
        #__ magic method is to identify the parameters and arguments
        #pass
        self.name=name
        
    def planets(self):
            print(f"{self.name} Welcome to the Solar System!!")
        
obj1=SolarSystem("Mercury") 
obj1.planets()  # "Method"- functions we define under class using objects of the class
print(type(obj1)) # <class '__main__.SolarSystem'>


# name1= "abc"
# name2= "def"
# print(type(name1)) # <class 'str'>

obj2=SolarSystem("Venus")
obj2.planets()
print(type(obj2))

    
    
class Car:
    def move_forward(self):
        print("car is moving forward")
        
car1=Car()
# car1.move_forward()
# print(dir(car1))   

