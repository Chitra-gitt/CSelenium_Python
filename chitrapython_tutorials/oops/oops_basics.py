'''
Created on 4 May 2025

@author: Chitra

Methods- are functions which are defined inside a class.
we can call methods using objects of that class


A method of one class can be called using an obj of the class

Constructor(__init__): It is a magic method used to construct an object,
by initializing it with specific values while creating the object.


'''


class SolarSystem(): 
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

    

