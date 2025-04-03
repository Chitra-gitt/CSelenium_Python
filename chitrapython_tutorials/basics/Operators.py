'''
Created on Mar 27, 2025

@author: Chitra

Operator: A symbol which performs operations on operands(variables)

Classifications based on operands:
1) Unary operator- Performs operation of single operand /variable
2) Binary operator- performs operation on two operand /variable
3) Ternary operator- performs operation on three operand /variable

Types of operators(Classifications based on operations)-

1) Assignment operator- '='
2) Arithmetic operator- "+,-,/,*,% (modulus),** (exponent), //(integer division)
3) Relational/comparison operator- ">,<,==(equal to), !=(not equal to)"
4) Logical operator- AND, OR, NOT
5) Membership operator- in, not in
6) Identity operators- is, is not
7) Unary minus operator- "- (negative integer)"

'''
print("==========Arithmetic operations=========")
a=67
b=890
d=67
c=a+b
print(f"addition of {a} and {b}:",a+b)
print(f"subtraction of {a} and {b}:",a-b)
print(f"multiplication of {a} and {b}:",a*b)
print(f"division of {a} and {b}:",a/b) #quotient of 2 numbers
print(f"modulus of {a} and {b}:", a%b) #reminder of 2 numbers
print(f"integer division of {a} and {b}:", a//b) #quotient of numbers converting into integer 
print(f"Square of {a} and {b}:", a**b)


print("==================Relational/comparison operator====================")
print(f"Is {a} greater than {b}?:", a>b)
print(f"Is {a} smaller than {b}?:", a<b)
print(f"Is {a} equal to {b}?:", a==b)
print(f"Is {a} not equal to {b}?:", a!=b)


print("=================Logical operator=============")
print("*****AND OPEARTOR*****")
print(True and False)
print(False and True)
print(True and True)
print(False and False)

print("*****OR OPEARTOR*****")
print(True or False)
print(False or True)
print(True or True)
print(False or False)

print("*****NOT OPEARTOR*****")
print(not True)
print(not False)

print("*******Membership operator*******")
print("a" in "alphabet")
print("i" in "alphabet")
print("1" in "alp1habet")
print("1" in "alphabet")
print("i" not in "alphabet")
print("A" in "alphabet")


print("*******Identity operator*******")
print(a is b)
print(a is not b)
print(a is d)
print('chitra' is 'Chitra')

e='chitra'
f= 'Chitra'


