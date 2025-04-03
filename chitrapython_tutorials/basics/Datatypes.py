'''
Created on Mar 25, 2025

@author: Chitra

data type: category to which i/o data belongs to
categorization of data helps us in memory allocation for efficient memory handling
'''
a=5
b=2
print(a+b)

c=9
d= 10
print(c*d)

# is used to stop executing, its basically used to comment 
'''
categories of data-types:
1. Built-in data-types: Data types already available in python
    a. Fundamental/ primary data types:
        i. int
        ii. float
        iii. complex - a+bj
        iv. bool (boolean) - True or False
        v. str (string) - "",''
        
    b. non-fundamental data types:
        i. list
        ii. tuple
        iii. set
        iv. dict
        v. bytes
        vi. bytearray
        
        2. User defined data types: Data types which are created by programmer

Commenting in Python:
1. Single line comments - #
2. Multi line comments - triple double/ single quotes.
'''
# int a = 3; --> java example
a = 3.0 # float
b = "abc" # string
c = 5 # integer
d = 4+7j #complex
e = True # boolean - True/False
# c = a+b

# print(c)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
# print(type(c))

g= 66-88j #complex (formula for complex datatype is complex= a+bj or a-bj ) it will not give any output its just a word
print(g)
print(type(g))


h=int(a)
print(h)
print(type(h))
print("converting float datatype into integer")

'''homework'''

#int()
#float()
#str()
#complex()
#bool()




