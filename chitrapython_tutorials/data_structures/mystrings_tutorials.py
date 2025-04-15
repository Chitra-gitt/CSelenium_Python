'''
Created on Apr 14, 2025

@author: Chitra

strings- words/phrase/sentence/paragraph

letters- character in python

string is a character / collection of characters

Strings are represented by '' or ""

string cannot be modified- its immutable
'''
from test.test_zoneinfo.test_zoneinfo import DRIVE

stdname="chitra"
print(stdname) #dont use "" here

print("stdname") #if we use "" then it will take it as string

print(type(stdname))

nick_name=''
print("nick_name:", nick_name)
print(type(nick_name))

age=55 #integer type 
# age="55" #string datatype
print("age:", age)
print(type(age))


#Access using Index

print(stdname[0])
print(stdname[1])
print(stdname[2])
print(stdname[3])
print(stdname[4])
print(stdname[5])

#Access using for loop

print("=======Access using for loop=======")
for letter in stdname:
    print(letter)


#Access using slicing operator- when we slice any collection

print("=======Access using for slicing operator=======")
print(stdname[1:5:1])
print(type(stdname[1:5:1]))

address= """ IQUEST
HEBBAL indUstrial area, MYSURU.
"""
print(address)

#Modification

#stdname[0]="z" #TypeError: 'str' object does not support item assignment

modified_stdname=stdname.replace('c', 'a')
print("name:", stdname)
print("modified name:", modified_stdname)


print(stdname.capitalize()) #capitalize() make the 1st letter as CAPITAL as index is 0 by default
print(stdname.strip().capitalize()) 
#strip() removes the (left and right indentation) called as leading and trailing spaces

print(address.casefold())

#casefold() function converts capital letter into small letters

print(stdname.upper())
#upper() function converts lower case to upper case

print(address.count('U'))


print(stdname.find('a')) #finds the index value


print(stdname.index('a'))
#index() raises value error when a substring is not found

print(stdname.isalnum())

name1= 'google drive' 

print(name1.split()) #split gives the space between the strings

stdname_list=["My","Name","is","chitra"]
stdname_sentence=('_'.join(stdname_list))

print(stdname_sentence)

print(len(stdname))







