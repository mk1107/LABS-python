'''
   Python program to demonstrate
   A. Any one loop
   B. Any one Condition
   C. 1 integer print
   D. 1 float print
   E. 1. string print
   F. 1 list print
   G. 1 tuple print
   H. Bonus is Use of Function
'''

for x in range (0,10):            # loop
    if(x%2==0):                   # condition
        print(x, end=' ')         # o/p is int
print ('\b',7/3)                  # o/p is float

print ("\nHELLO WORLD")             # o/p is string

L = ['MK','_',11,"_",0,7]  # Creating a List with mixed type of values (Having numbers and strings) 

print("\nList with the use of Mixed Values: ",L)


T = ('MK','_',11,"_",0,7)  # Creating a tuple with mixed type of values (Having numbers and strings) 
print("\nTuple with the use of Mixed Values: ",T)


def printme( str ):        # Function definition is here (This prints a passed string into this function)
   print (str)
   return

printme("\nCall to user defined function!") # Call printme Function
