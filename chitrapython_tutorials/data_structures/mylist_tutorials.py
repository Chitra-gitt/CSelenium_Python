'''
Created on Apr 6, 2025

@author: Chitra

List: is a data structure represented by []

1. Creation of list
-empty list can be created

-list with elements:
>manually adding elements
>using in-built function called list()

#1.creation of list
#a. creation of empty list

2. list of hetrogenous
a=[]
print(type(a))

tuple cannot be modified once created/immutable
set is mutable
#b. creation of list with elements

3. accessing

List: Is a data structure represented by []

1. Creation of list
    - Empty list can be created
    - List with elements:
        > Manually adding elements
        > Using in-built function called list()
2. List is heterogeneous
3. Accessing elements
    - Indexing/ Using Index
    - Using slicing operator
    - Using loops
4. List can be modified
5. List stores None as a value
6. List stores duplicate values
7. Insertion order is preserved
8. The size of a list is not fixed or constant
tuple cannot be modified once created/immutable
set is mutable- can be modified
'''

b= [1,2,3,4,5] #homogenous datastructure #list represented as square bracket
print (type(b))
print(b)


b= {1,2,3,4,5} #set represented as curly bracket
print (type(b))
print(b)

b= (1,2,3,4,5) #tuple represented as round bracket
print (type(b))
print(b)

c=[1,"abc",5.33,True,6+9j]#hetrogenous datastructure # diff types of data types
print(c)

d=list(range(1,20))
print(d)

# accessing the elements using index

print(c[4]) #to fetch the last number

print(c[0])
print(c[-1]) #to fetch the last number

# Modification/replacement using index-

c[1]= 'chitra' #re-initialization
print(c)

#slicing operator:- list_name[start:stop:step]--> takes index as input
#default value start- 0 Zero 
#stop value- last value
#step: 1



print(c[::])

print(d[::])

print(d[3:9])

print(d[:12]) #start value is 0 index
print(d[6:]) # last value index

print(d[-12:-6]) #takes -12 and -7th index value


print(d[::2])

print(d[::-2]) 

print(d[::-1]) #reverse the list

print(d[-12:-6:-1]) #empty list
 
print(d[-6:-12:-1])  #start value should be greater than stop value

d=list(range(-1,-20,-1))
print(d)



#accessing using loops

print(c)
#for loop:
print("==for loop==")
for ele in c:
    print(ele)
    
print("==while loop==")

i=0

while i<len(d):
    print(d[i])
    i+=1
    
    
    
    print(c[0])
    print(c[1])
    print(c[2])
    print(c[3])
    print(c[4])
    
#finding odd number
p=list(range(20))
for q in p:
    if q%2==1:
        print(q)
        

#print letter 'a' from the below words-
    
e=["Bhavani", "Chitra", "Sandeep", "Sanjana", "Vivek", "Yogitha"]

for f in e:
   
   if 'a' in f:
    print(f)
    #print(f)

print(len(c)) #finding the length of collection
   
e=["Bhavani", "chitra", "Sandeep", "Sanjana", "Vivek", "Yogitha", None, "chitra"]

print(e)
   
e.append("Manju") #adding an item
print(e)
    
e.insert(5,"iquest") # insert an item in between the list
print(e)

e.append(c) #combining both the lists
print(e)


# practicing 

z=[]
print(type(z))

y=[15,30,45,22,10,60,13]

for x in y:
    if x%2==1:
        
        #print('odd numbers are:-->',x)
        #print('square of odd numbers are:-->',x**2)
        z.append(x**2)
print(z)

e.append(c)
print(e)       
   
print(c.index(5.33))
print('e.count("chitra"):', e.count("chitra"))
print('e.index("chitra"):', e.index("chitra"))


''' ques- find the indices of the elements in the list?

sol-

'''

print('c-->',c)
print(c.pop(2)) #pop will remove the particular value present in the list and also return what value is removed
print(c.remove("chitra"))
print(c)
print(c.remove(True))
print(c)
print('c.pop()', c.pop())
print(c)
c.remove(True)
print(c)

















