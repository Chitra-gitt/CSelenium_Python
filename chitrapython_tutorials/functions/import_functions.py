'''
Created on 3 May 2025

@author: Chitra
'''
from functions.functions_arguments import addition #import statement

addition(10,20,30)

from functions.functions_arguments import addition,cal_energy #to call multiple functions
cal_energy(10)

from functions.functions_arguments import *  #to call all the functions from the module we use *
addition(10,20,30)
cal_energy(10)
subtraction(b=10, a=20)

from functions.functions_arguments import cal_energy as ce #ce is the alias of cal_energy
ce(5)

